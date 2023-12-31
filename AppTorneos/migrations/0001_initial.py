# Generated by Django 4.2.4 on 2023-09-02 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('barrio', models.CharField(max_length=30)),
                ('titulos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('club', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AppTorneos.equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Entrenadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('titulos', models.IntegerField()),
                ('edad', models.IntegerField()),
                ('club', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AppTorneos.equipo')),
            ],
        ),
    ]
