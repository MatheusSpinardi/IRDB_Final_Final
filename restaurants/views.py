from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Restaurant
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Restaurant, Resenha
from .forms import RestaurantForm, ResenhaForm

def detail_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    context = {'restaurant': restaurant}
    return render(request, 'restaurants/detail.html', context)

class RestaurantListView(generic.ListView):
    model = Restaurant
    template_name = 'restaurants/index.html'


def search_restaurants(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        restaurant_list = Restaurant.objects.filter(name__icontains=search_term)
        context = {"restaurant_list": restaurant_list}
    return render(request, 'restaurants/search.html', context)
    

def create_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            restaurant_name = form.cleaned_data['name']
            restaurant_poster_url = form.cleaned_data['poster_url']
            restaurant = Restaurant(name=restaurant_name,                        
                          poster_url=restaurant_poster_url)
            restaurant.save()
            return HttpResponseRedirect(
                reverse('restaurants:detail', args=(restaurant.id, )))
    else:
        form = RestaurantForm()
    context = {'form': form}
    return render(request, 'restaurants/create.html', context)


def update_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            restaurant.name = form.cleaned_data['name']
            restaurant.poster_url = form.cleaned_data['poster_url']
            restaurant.save()
            return HttpResponseRedirect(
                reverse('restaurants:detail', args=(restaurant.id, )))
    else:
        form = RestaurantForm(
            initial={
                'name': restaurant.name,
                'poster_url': restaurant.poster_url
            })

    context = {'restaurant': restaurant, 'form': form}
    return render(request, 'restaurants/update.html', context)

def delete_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

    if request.method == "POST":
        restaurant.delete()
        return HttpResponseRedirect(reverse('restaurants:index'))

    context = {'restaurant':restaurant}
    return render(request, 'restaurants/delete.html', context)

def create_resenha(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    if request.method == 'POST':
        form = ResenhaForm(request.POST)
        if form.is_valid():
            resenha_author = form.cleaned_data['author']
            resenha_text = form.cleaned_data['text']
            resenha = Resenha(author=resenha_author,
                            text=resenha_text,
                            movie=restaurant)
            resenha.save()
            return HttpResponseRedirect(
                reverse('restaurants:detail', args=(restaurant_id, )))
    else:
        form = ResenhaForm()
    context = {'form': form, 'restaurant': restaurant}
    return render(request, 'restaurants/review.html', context)

