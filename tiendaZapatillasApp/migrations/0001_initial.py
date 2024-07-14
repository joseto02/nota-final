# Generated by Django 4.1.2 on 2024-07-13 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido_paterno', models.CharField(max_length=25)),
                ('apellido_materno', models.CharField(max_length=25)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id_compra', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_compra', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id_marca', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_marca', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Zapatilla',
            fields=[
                ('id_zapatilla', models.AutoField(primary_key=True, serialize=False)),
                ('precio', models.IntegerField()),
                ('talla', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('rut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendaZapatillasApp.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Modelo_zapatilla',
            fields=[
                ('id_modelo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_modelo', models.CharField(max_length=100)),
                ('id_marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendaZapatillasApp.marca')),
            ],
        ),
        migrations.AddField(
            model_name='marca',
            name='id_zapatilla',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendaZapatillasApp.zapatilla'),
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant_unidades', models.IntegerField()),
                ('sub_total', models.IntegerField()),
                ('total', models.IntegerField()),
                ('id_compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendaZapatillasApp.compra')),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='id_zapatilla',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tiendaZapatillasApp.zapatilla'),
        ),
    ]
