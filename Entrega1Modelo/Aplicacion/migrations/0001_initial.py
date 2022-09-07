# Generated by Django 4.1 on 2022-09-07 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50)),
                ('articuloTitulo', models.TextField(max_length=50)),
                ('articuloContenido', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('mensaje', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.TextField(max_length=40)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=40)),
            ],
        ),
    ]
