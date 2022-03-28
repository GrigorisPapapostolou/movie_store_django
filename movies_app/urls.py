from django.urls import path,include
from movies_app.views import AvailableMovieList, MovieDetailsView, RentMovieView, ReturnMovieView, Logout, Registration
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('account/login/', obtain_auth_token, name='login'),
    path('account/register/', Registration, name='register'),
    path('account/logout/', Logout, name='logout'),
    path('movie/available/list', AvailableMovieList.as_view(),name='movie-list'),
    path('movie/<int:pk>/detail', MovieDetailsView.as_view(),name='movie-details'),
    path('movie/<int:pk>/rent', RentMovieView.as_view(), name='movie-rent'),
    path('movie/<int:pk>/return', ReturnMovieView.as_view(), name='movie-return')
]
