# Generated by Django 3.2.4 on 2021-06-17 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rayoMakween', '0004_auto_20210617_0130'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajo',
            name='comentario',
            field=models.TextField(default='--'),
        ),
    ]
