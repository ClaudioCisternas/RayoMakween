# Generated by Django 3.2.4 on 2021-06-22 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rayoMakween', '0007_galeria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='galeria',
            old_name='Trabajo',
            new_name='trabajo',
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='imagen',
            field=models.ImageField(default='trabajos/defecto,jpg', upload_to='trabajos'),
        ),
    ]
