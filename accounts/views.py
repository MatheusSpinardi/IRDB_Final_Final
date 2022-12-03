from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group                  # adicione esta linha
from .forms import RestauranteForm,ClienteForm

def signup(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            user = form.save()                                # edite esta linha
            user_group = Group.objects.get(name='cliente') # edite esta linha
            user.groups.add(user_group)                       # edite esta linha

            return HttpResponseRedirect(reverse('login'))
    else:
        form = ClienteForm()

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

def signupR(request):
    if request.method == 'POST':
        form = RestauranteForm(request.POST)
        if form.is_valid():
            user = form.save()                                # edite esta linha
            user_group = Group.objects.get(name='restaurante') # edite esta linha
            user.groups.add(user_group)                       # edite esta linha

            return HttpResponseRedirect(reverse('login'))
    else:
        form =  RestauranteForm()

    context = {'form': form}
    return render(request, 'accounts/signupR.html', context)