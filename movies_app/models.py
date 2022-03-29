from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        #  create tokens for your users
        Token.objects.create(user=instance)


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class Movie(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    created = models.DateField()
    rating = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)],)    
    director = models.CharField(max_length=50, null=True, blank=True)
    genre = models.ManyToManyField(Category)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Rental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,related_name='rentals')
    rental_date = models.DateTimeField(auto_now_add=True, null=True)
    return_date = models.DateTimeField(null=True)
    paid_amount = models.FloatField(null=True)

