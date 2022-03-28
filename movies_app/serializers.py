from rest_framework import serializers
from movies_app.models import  Category, Movie, Rental
from django.contrib.auth.models import User
from django.utils import timezone

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.ListSerializer(child=serializers.CharField())
    class Meta:
        model = Movie
        fields = "__all__"

class MovieListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="movie-details")
    genre = serializers.ListSerializer(child=serializers.CharField())
    class Meta:
        model = Movie
        fields = ['url','title','storyline','created','genre']

def calculate_amount(x):
     return x * 1.0 if x <= 3 else 3.0 + (x-3) * 0.5

class RentalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rental
        fields = "__all__"
        extra_kwargs = {'user': {'required': False},'movie': {'required': False}}

    def update(self, instance, validated_data):
        instance.return_date = timezone.now()
        instance.paid_amount = calculate_amount((instance.return_date - instance.rental_date).days)
        instance.save()
        return instance

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {'password' : {'write_only': True}}
    
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': 'Password does not match!'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'Account already exists!'})

        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account




