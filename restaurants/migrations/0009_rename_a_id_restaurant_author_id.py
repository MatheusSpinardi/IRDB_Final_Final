# Generated by Django 4.1.3 on 2022-12-03 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0008_restaurant_a_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='a_id',
            new_name='author_id',
        ),
    ]
