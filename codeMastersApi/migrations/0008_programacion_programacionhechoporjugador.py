# Generated by Django 4.0.5 on 2022-07-03 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('codeMastersApi', '0007_rename_hechoporjugador_documentacionhechoporjugador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEjercicio', models.CharField(max_length=200)),
                ('ejercicio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProgramacionHechoPorJugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.TextField()),
                ('revisado', models.BooleanField(default=False)),
                ('correcto', models.BooleanField(default=False)),
                ('programacionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codeMastersApi.programacion')),
                ('usuarioId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]