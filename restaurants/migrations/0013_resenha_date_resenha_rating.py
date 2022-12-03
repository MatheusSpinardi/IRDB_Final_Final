# Generated by Django 4.1.3 on 2022-12-03 16:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0012_delete_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='resenha',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resenha',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]
