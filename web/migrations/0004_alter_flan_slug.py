# Generated by Django 3.2.4 on 2024-08-07 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flan',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
