# Generated by Django 3.2.2 on 2021-05-17 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autotravel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='news/', verbose_name='Зображення новини')),
                ('title', models.CharField(max_length=200, verbose_name='Заговолок')),
                ('descriptions', models.TextField(verbose_name='Короткий опис')),
                ('description', models.TextField(verbose_name='Опис 1')),
                ('image1', models.ImageField(upload_to='news/', verbose_name='Додаткове фото 1')),
                ('image2', models.ImageField(upload_to='news/', verbose_name='Додаткове фото 2')),
                ('image3', models.ImageField(upload_to='news/', verbose_name='Додаткове фото 3')),
                ('image4', models.ImageField(upload_to='news/', verbose_name='Додаткове фото 4')),
                ('descriptione', models.TextField(verbose_name='Опис 2')),
                ('url', models.SlugField(max_length=130, unique=True)),
            ],
            options={
                'verbose_name': 'Новини',
                'verbose_name_plural': 'Новини',
            },
        ),
    ]
