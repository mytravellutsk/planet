from django.db import models
from datetime import date

from django.urls import reverse


class Movie(models.Model):
    title = models.CharField("Назва", max_length=100)
    tagline = models.CharField("Тег", max_length=100, default='')
    description = models.TextField("Опис")
    poster = models.ImageField("Постер", upload_to="movies/")
    year = models.PositiveSmallIntegerField("Дата виходу", default=2019)
    country = models.CharField("Країна", max_length=30)
    budget = models.PositiveIntegerField("Бюджет", default=0, help_text="вказувати суму в доларах")
    fees_in_usa = models.PositiveIntegerField(
        "Збори в США", default=0, help_text="Вказувати суму в доларах"
    )
    fees_in_world = models.PositiveIntegerField(
        "Збори в Світі", default=0, help_text="Вказувати суму в доларах"
    )
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Чорновик", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фільм"
        verbose_name_plural = "Фільми"


class NewsList(models.Model):
    image = models.ImageField("Зображення новини", upload_to="news/")
    title = models.CharField('Заговолок', max_length=200)
    descriptions = models.TextField("Короткий опис")
    description = models.TextField("Опис 1")
    image1 = models.ImageField("Додаткове фото 1", upload_to="news/")
    image2 = models.ImageField("Додаткове фото 2", upload_to="news/")
    image3 = models.ImageField("Додаткове фото 3", upload_to="news/")
    image4 = models.ImageField("Додаткове фото 4", upload_to="news/")
    descriptione = models.TextField("Опис 2")
    #date = models.DateField(default=date.today())
    url = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новини"
        verbose_name_plural = "Новини"