# Generated by Django 3.2.8 on 2021-10-09 22:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_pelicula_sinopsis'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='fecha_estreno',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]