# Generated by Django 3.2.2 on 2021-05-11 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210511_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='newslist',
            name='url',
            field=models.SlugField(default=2, max_length=130, unique=True),
            preserve_default=False,
        ),
    ]
