# Generated by Django 5.1.3 on 2024-11-29 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='marcas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_marcas', models.IntegerField()),
                ('id_sucursal', models.IntegerField()),
                ('id_producto', models.IntegerField()),
                ('Nombre_Marca', models.CharField(max_length=100)),
                ('Numtelefono', models.IntegerField()),
                ('Correo', models.CharField(max_length=100)),
            ],
        ),
    ]