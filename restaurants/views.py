from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.
from django.http import HttpResponse, HttpRequest
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Restaurant, Resenha, Reserva
from .forms import RestaurantForm, ResenhaForm, ReservaForm, ReservaUpdateForm
from django.contrib import messages


def detail_restaurant(request: HttpRequest, restaurant_id) -> HttpResponse:
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    

    context = {'restaurant': restaurant}
    return render(request, 'restaurants/detail.html', context)


def meu_restaurant(request,user_id):
    context= {}
    search_list = Restaurant.objects.filter(author_id=user_id)
    if len(search_list) == 1:
        restaurant = get_object_or_404(Restaurant, author_id=user_id)
        context = {'restaurant': restaurant}
    return render(request, 'restaurants/meurestaurante.html', context)

    

class RestaurantListView(generic.ListView):
    model = Restaurant
    template_name = 'restaurants/index.html'


def search_restaurants(request):

    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        search_list = Restaurant.objects.filter(name__icontains=search_term)
        context = {"search_list": search_list,}

    if request.GET.get('query2', False):
        search_term = request.GET['query2'].lower()
        search_list = Restaurant.objects.filter(comida__icontains=search_term)
        context = {"search_list": search_list,}
    else:
        restaurant_list = Restaurant.objects.all()
        context = {"restaurant_list":restaurant_list}
    return render(request, 'restaurants/search.html', context)
    
@login_required
@permission_required('restaurants.add_restaurant')
def create_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            restaurant_name = form.cleaned_data['name']
            restaurant_author_id = request.user.id
            restaurant_poster_url = form.cleaned_data['poster_url']
            restaurant_endereco = form.cleaned_data['endereco']
            restaurant_comida = form.cleaned_data['comida']
            restaurant_preco = form.cleaned_data['preco']
            restaurant_text = form.cleaned_data['text']
            restaurant = Restaurant(name=restaurant_name,                        
                          poster_url=restaurant_poster_url,
                          author_id=restaurant_author_id,
                          endereco=restaurant_endereco,
                          comida=restaurant_comida,
                          preco=restaurant_preco,
                          text = restaurant_text)
            restaurant.save()
            context = {'restaurant': restaurant}
            return render(request, 'restaurants/meurestaurante.html', context)

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
            restaurant.endereco = form.cleaned_data['endereco']
            restaurant.comida = form.cleaned_data['comida']
            restaurant.preco = form.cleaned_data['preco']
            restaurant.text = form.cleaned_data['text']
            restaurant.save()
            context = {'restaurant': restaurant}
            return render(request, 'restaurants/meurestaurante.html', context)
    else:
        form = RestaurantForm(
            initial={
                'name': restaurant.name,
                'poster_url': restaurant.poster_url,
                'endereço':restaurant.endereco,
                'comida':restaurant.comida,
                'preco':restaurant.preco,
                'text':restaurant.text
            })

    context = {'restaurant': restaurant, 'form': form}
    return render(request, 'restaurants/update.html', context)

def delete_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

    if request.method == "POST":
        restaurant.delete()
        context={'restaurant': None}
        return render(request, 'restaurants/meurestaurante.html', context)

    context = {'restaurant':restaurant}
    return render(request, 'restaurants/delete.html', context)

@login_required
@permission_required('restaurants.add_resenha')
def create_resenha(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    if request.method == 'POST':
        form = ResenhaForm(request.POST)
        if form.is_valid():
            resenha_author = request.user
            resenha_text = form.cleaned_data['text']
            resenha_rating = form.cleaned_data['rating']
            resenha = Resenha(author=resenha_author,
                            text=resenha_text,
                            restaurant=restaurant,
                            rating=resenha_rating)
            resenha.save()
            restaurant.avr= restaurant.average_rating()
            restaurant.save()
            return HttpResponseRedirect(
                reverse('restaurants:detail', args=(restaurant_id, )))
    else:
        form = ResenhaForm()
    context = {'form': form, 'restaurant': restaurant}
    return render(request, 'restaurants/resenha.html', context)

def reserva_restaurant(request: HttpRequest, restaurant_id) -> HttpResponse:
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    

    context = {'restaurant': restaurant}
    return render(request, 'restaurants/reserva.html', context)

@login_required
@permission_required('restaurants.add_reserva')
def create_reserva(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva_cliente = request.user
            reserva_cpf = form.cleaned_data['cpf']
            reserva_np = form.cleaned_data['np']
            reserva_reserva = form.cleaned_data['reserva']
            reserva = Reserva(cliente=reserva_cliente,
                            cpf=reserva_cpf,
                            restaurant=restaurant,
                            np=reserva_np,
                            reserva= reserva_reserva)
            reserva.save()
            return HttpResponseRedirect(
                reverse('restaurants:reserva', args=(restaurant_id, )))
    else:
        form = ReservaForm()
    context = {'form': form, 'restaurant': restaurant}
    return render(request, 'restaurants/reservacreate.html', context)

@login_required
@permission_required('restaurants.change_reserva')
def update_reserva(request, reserva_id):
    reserva= get_object_or_404(Reserva, pk=reserva_id)
    restaurant = get_object_or_404(Restaurant, pk=reserva.restaurant.id)
    if request.method == "POST":
        form = ReservaUpdateForm(request.POST)
        if form.is_valid():

            reserva.standby=1
            reserva.aprove= form.cleaned_data['aprove']
            

            reserva.save()
            context = {'restaurant': restaurant}
            return render(request, 'restaurants/reserva.html', context)
    else:
        form = ReservaUpdateForm(
            initial={
                'aprove':reserva.aprove,
                
            })

    context = {'reserva': reserva, 'form': form}
    return render(request, 'restaurants/reservaup.html', context)

def minhas_reserva(request, user_id):
    context= {}
    reserva_list = Reserva.objects.filter(cliente_id=user_id)
    context = {'reserva_list': reserva_list}
    return render(request, 'restaurants/minhasreservas.html', context)
# @login_required
# @permission_required('restaurants.add_resenha')
# def submit_resenha(request, restaurant_id):
#     url = request.META.get('HTTP_REFERER')
#     if request.method == 'POST':
#         try:
#             resenhas = Resenha.objects.get(author__id=request.user.id, restaurant__id=restaurant_id)
#             form = ResenhaForm(request.POST, instance=resenhas)
#             form.save()
#             messages.success(request, 'Thank you! Your review has been updated.')
#             return redirect(url)
#         except Resenha.DoesNotExist:
#             form = ResenhaForm(request.POST)
#             if form.is_valid():
#                 data = Resenha()
#                 data.rating = form.cleaned_data['rating']
#                 data.text = form.cleaned_data['text']
                
#                 data.restaurant_id = restaurant_id
#                 data.author_id = request.user.id
#                 data.save()
#                 messages.success(request, 'Thank you! Your review has been submitted.')
#                 return redirect(url)