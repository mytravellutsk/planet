# Generated by Django 3.2.2 on 2021-05-12 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20210512_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='world_premiere',
        ),
    ]