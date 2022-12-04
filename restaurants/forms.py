from django.forms import ModelForm
from .models import Restaurant, Resenha, Reserva


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
            'name': 'Nome do Restaurante',
            'poster_url': 'URL do logo',
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

class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        fields = [
            
            'cpf',
            'np',
            'reserva',
        ]
        labels = {
            'cpf': 'CPF',
            'np': 'Número de pessoas',
            'reserva': 'Dia  e hora da reserva: (Mês/Dia/Ano xx:xx)  ',
        }

class ReservaUpdateForm(ModelForm):
    class Meta:
        model = Reserva
        fields = [
            
            'aprove',
            
            
        ]
        labels = {
            'aprove': 'Aprovado?',
            
        }