# Generated by Django 4.1.5 on 2023-01-03 15:32

from django.db import migrations
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('apiModel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='names',
            field=picklefield.fields.PickledObjectField(default='', editable=False),
        ),
        migrations.DeleteModel(
            name='Suggestions',
        ),
    ]
