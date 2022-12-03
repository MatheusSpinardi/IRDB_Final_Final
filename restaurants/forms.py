from django.forms import ModelForm
from .models import Restaurant, Resenha


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'poster_url',
        ]
        labels = {
            'name': 'Título',
            'poster_url': 'URL do Poster',
        }

class ResenhaForm(ModelForm):
    class Meta:
        model = Resenha
        fields = [
            
            'text',
            'rating',
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Resenha',
        }