# Generated by Django 5.1.5 on 2025-02-01 09:58

import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0002_category_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='recipe',
            name='status',
            field=models.CharField(choices=[('D', 'Draft'), ('P', 'Published')], default=1, max_length=2),
            preserve_default=False,
        ),
    ]
