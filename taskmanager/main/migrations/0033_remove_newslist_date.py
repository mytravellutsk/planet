# Generated by Django 3.2.2 on 2021-08-14 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_alter_newslist_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newslist',
            name='date',
        ),
    ]