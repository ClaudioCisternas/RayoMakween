# Generated by Django 3.2.4 on 2021-06-13 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rayoMakween', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajo',
            fields=[
                ('nombre', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('diagnostico', models.TextField()),
                ('fecha', models.DateField()),
                ('Materiales', models.TextField()),
                ('mecanico', models.CharField(max_length=50)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rayoMakween.tipotrabajo')),
            ],
        ),
    ]
