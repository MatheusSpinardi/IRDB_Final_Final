# Generated by Django 4.1.3 on 2022-12-03 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0014_alter_resenha_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resenha',
            old_name='date',
            new_name='data',
        ),
    ]
