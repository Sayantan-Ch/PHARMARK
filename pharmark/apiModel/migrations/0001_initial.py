# Generated by Django 4.1.5 on 2023-01-03 12:39

import apiModel.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggestionCode', models.CharField(default=apiModel.models.generate_unique_code, max_length=5, unique=True)),
                ('drugCode', models.CharField(default='', max_length=5, unique=True)),
                ('Approved', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Suggestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, unique=True)),
                ('suggestionCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiModel.drug')),
            ],
        ),
    ]
