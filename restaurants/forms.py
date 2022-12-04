from django.forms import ModelForm
from .models import Restaurant, Resenha


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'poster_url',
            'endereco',
            'comida',
            'preco',
            'text',
        ]
        labels = {
            'name': 'Título',
            'poster_url': 'URL do Poster',
            'endereco': 'Endereço',
            'comida': 'Tipo de comida',
            'preco': 'Faixa de preço',
            'text': 'Descrição do lugar',
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