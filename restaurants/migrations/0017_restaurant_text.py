# Generated by Django 4.1.3 on 2022-12-04 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0016_restaurant_comida_restaurant_endereco_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='text',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
