# Generated by Django 3.2.4 on 2021-06-14 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rayoMakween', '0002_trabajo'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajo',
            name='imagen',
            field=models.ImageField(null=True, upload_to='trabajos'),
        ),
    ]