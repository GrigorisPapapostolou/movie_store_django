from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from movies_app import serializers
from movies_app import models


class MovieTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.category = models.Category.objects.create(title="Adventure")
        self.movie = models.Movie.objects.create(title="Example", storyline="Example",created="2022-03-29",rating=5,director="Example",available=True)
    
    def test_movies_list(self):
        response = self.client.get(reverse('movie-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_movie_details(self):
        response = self.client.get(reverse('movie-details', args=(self.movie.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class RentTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.category = models.Category.objects.create(title="Adventure")
        self.movie = models.Movie.objects.create(title="Example", storyline="Example",created="2022-03-29",rating=5,director="Example",available=True)
        #self.rental = models.Rental.objects.create(user=self.user,movie=self.movie, rental_date="2022-03-29")

    def test_rent_movie(self):
        response = self.client.post(reverse('movie-rent', args=(self.movie.id,)))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ReturnTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.category = models.Category.objects.create(title="Adventure")
        self.movie = models.Movie.objects.create(title="Example", storyline="Example",created="2022-03-29",rating=5,director="Example",available=False)
        self.rental = models.Rental.objects.create(user=self.user, movie=self.movie, rental_date="2022-03-29")

    def test_rent_movie(self):
        response = self.client.put(reverse('movie-return', args=(self.movie.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


