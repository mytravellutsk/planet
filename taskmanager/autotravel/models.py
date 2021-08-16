from django.db import models


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


class Travels(models.Model):
    image = models.ImageField("Зображення фото туру", upload_to="travel/")
    title = models.CharField('Заговолок', max_length=200)
    uan = models.CharField("Ціна", max_length=5)
    eat = models.CharField('Харчування', max_length=200)
    day = models.CharField('Кількість днів', max_length=200)
    video = models.CharField('Ссилка на відео', max_length=300)
    description = models.TextField("Програма туру")
    image1 = models.ImageField("Додаткове фото 1", upload_to="travel/")
    image2 = models.ImageField("Додаткове фото 2", upload_to="travel/")
    image3 = models.ImageField("Додаткове фото 3", upload_to="travel/")
    image4 = models.ImageField("Додаткове фото 4", upload_to="travel/")
    descriptione = models.TextField("Опис проживання 2")
    image5 = models.ImageField("Фото проживання 1", upload_to="travel/")
    image6 = models.ImageField("Фото проживання 2", upload_to="travel/")
    image7 = models.ImageField("Фото проживання 3", upload_to="travel/")
    image8 = models.ImageField("Фото проживання 4", upload_to="travel/")
    descriptions = models.TextField("У вартість входить: ")
    date = models.CharField('Дати виїздів', max_length=200)
    url = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Автобусний тур нові"
        verbose_name_plural = "Автобусні нові"