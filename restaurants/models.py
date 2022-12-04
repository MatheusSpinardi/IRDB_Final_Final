from django.db import models

# Create your models here.
from django.conf import settings
from django.db.models import Avg
from django.contrib.auth.models import User


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    poster_url = models.URLField(max_length=200, null=True)
    author_id = models.IntegerField(default=0)
    endereco = models.CharField(max_length=255, blank= True)
    comida = models.CharField(max_length=255, blank= True)
    preco = models.CharField(max_length=255, blank= True)
    text = models.TextField(max_length=500, blank= True)

    
    def average_rating(self) -> float:
        return Resenha.objects.filter(restaurant=self).aggregate(Avg("rating"))["rating__avg"] or 0

    def __str__(self):
        return f'{self.name}'
    

class Resenha(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=500, blank= True)
    likes = models.IntegerField(default=0)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.FloatField(default=0)
    data=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'

