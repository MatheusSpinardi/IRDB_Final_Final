from django.contrib import admin

# Register your models here.
from .models import Restaurant, Resenha, Reserva

admin.site.register(Restaurant)
admin.site.register(Resenha)
admin.site.register(Reserva)