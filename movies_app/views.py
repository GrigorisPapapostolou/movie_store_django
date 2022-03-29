from movies_app.models import Movie, Rental
from rest_framework.permissions import IsAuthenticated
from movies_app.serializers import MovieSerializer, MovieListSerializer, MovieListSerializer,RegistrationSerializer, RentalSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView,UpdateAPIView,RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.utils import timezone
from django.core.cache import cache
'''
Use Case: List all the available movies based on :
    - user query     (search)
    - movie category (filter)
'''
class AvailableMovieList(ListAPIView):
    page_size = 5
    page_size_query_param = 'page_size'
    permission_classes = [IsAuthenticated]
    serializer_class = MovieListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]  
    filterset_fields = ['genre__title'] 
    search_fields  = ['title', 'storyline', 'director']

    def get_queryset(self):
        return  Movie.objects.filter(available=True)


'''
Use Case: Get details of a specific movie
'''
class MovieDetailsView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MovieSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        
        if cache.get(pk):
            movie = cache.get(pk)
            print("Data from cache")
        else:
            movie = Movie.objects.filter(pk=pk)
            cache.set(pk,movie)
            print("Data from db")

        return movie


'''
Use Case: Rent a movie
'''
class RentMovieView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RentalSerializer
    queryset = Rental.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        user = self.request.user
        movie = Movie.objects.get(pk=pk)

        if movie.available == False:
            raise ValidationError("Movie is not available!")

        rental_queryset = Rental.objects.filter(movie=movie, user=user, return_date__isnull=True)

        if rental_queryset.exists():
            raise ValidationError("You have already rented this movie!")

        movie.available = False
        movie.save()
        serializer.save(movie = movie,user=user)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({"response": "Movie successfully rented!"}, status=status.HTTP_201_CREATED)


'''
Use Case: Return and Pay for movie
'''
class ReturnMovieView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RentalSerializer
        
    def get_object(self):
        user = self.request.user
        pk = self.kwargs.get('pk')
        movie = Movie.objects.get(pk=pk)
        rental_movie = Rental.objects.filter(movie=movie, user=user, return_date__isnull=True)
        if rental_movie.exists() == False:
            raise ValidationError("You have not rented this movie!")
        movie.available = True
        movie.save()
        return  rental_movie.first()
   
    
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({"response": "Movie successfully returned!"}, status=status.HTTP_200_OK)


'''
User Registration Process with Token authentication
'''
@api_view(['POST',])
def Logout(request):

    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['POST',])
def Registration(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = "Registration Successful!"
            data['username'] = account.username
            data['email'] = account.email
            token = Token.objects.get(user=account).key
            data['token'] = token

        else:
            data = serializer.errors
        
        return Response(data, status=status.HTTP_201_CREATED)