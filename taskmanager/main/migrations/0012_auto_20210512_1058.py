# Generated by Django 3.2.2 on 2021-05-12 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210512_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='actors',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.DeleteModel(
            name='Actor',
        ),
    ]
