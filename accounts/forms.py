from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ClienteForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nome = forms.CharField(required=True)
    sobrenome = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username","nome","sobrenome", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(ClienteForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["nome"]
        user.last_name = self.cleaned_data["sobrenome"]
        if commit:
            user.save()
        return user

class RestauranteForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(RestauranteForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
        return user