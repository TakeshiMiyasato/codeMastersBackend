# Generated by Django 4.0.5 on 2022-07-03 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codeMastersApi', '0008_programacion_programacionhechoporjugador'),
    ]

    operations = [
        migrations.AddField(
            model_name='programacion',
            name='puntaje',
            field=models.IntegerField(default=1),
        ),
    ]
