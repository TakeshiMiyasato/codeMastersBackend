# Generated by Django 4.0.5 on 2022-06-29 03:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('codeMastersApi', '0005_alter_documentacion_preguntaquizz'),
    ]

    operations = [
        migrations.CreateModel(
            name='HechoPorJugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documentacionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='codeMastersApi.documentacion')),
                ('usuarioId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
