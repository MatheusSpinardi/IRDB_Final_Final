from django.urls import path

from . import views


app_name = 'restaurants'
urlpatterns = [
    path('', views.RestaurantListView.as_view(), name='index'),
    path('search/', views.search_restaurants, name='search'),
    path('create/', views.create_restaurant, name='create'),
    path('<int:restaurant_id>/', views.detail_restaurant, name='detail'), # adicione esta linha
    path('update/<int:restaurant_id>/', views.update_restaurant, name='update'),
    path('delete/<int:restaurant_id>/', views.delete_restaurant, name='delete'),
    path('<int:restaurant_id>/resenha/', views.create_resenha, name='resenha'),
]
