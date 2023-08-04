# Generated by Django 4.1.7 on 2023-08-04 01:22

import colorfield.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='название')),
                ('measurement_unit', models.CharField(max_length=200, verbose_name='единица измерения')),
            ],
            options={
                'verbose_name': 'ингредиент',
                'verbose_name_plural': 'ингредиенты',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='название')),
                ('color', colorfield.fields.ColorField(blank=True, default='#FFFFFF', image_field=None, max_length=7, null=True, samples=None, verbose_name='цвет')),
                ('slug', models.CharField(max_length=200, null=True, unique=True, validators=[django.core.validators.RegexValidator(regex='^[-а-я-a-zA-Z0-9_]+$')], verbose_name='слаг')),
            ],
            options={
                'verbose_name': 'тег',
                'verbose_name_plural': 'теги',
            },
        ),
    ]
