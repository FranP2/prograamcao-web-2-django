# Generated by Django 5.1 on 2024-08-17 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cidade',
            name='estado',
        ),
        migrations.AddField(
            model_name='estado',
            name='cidades',
            field=models.ManyToManyField(to='aa.cidade'),
        ),
    ]
