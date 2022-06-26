from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор рецепта',
        related_name='recipes',
    )
    ingredients = models.ManyToManyField(
        'Ingredient',
        verbose_name='Ингредиенты',
        # through='Ingredient'
        related_name='recipes'
    )
    tags = models.ManyToManyField(
        'Tag',
        verbose_name='Тег',
        # through='Tag',
        related_name='recipes',
    )
    image = models.ImageField(
        'Изображение рецепта',
        upload_to='recipes/',
    )
    name = models.CharField(
        'Название рецепта',
        max_length=200,
    )
    text = models.TextField(
        'Описание рецепта',
    )
    cooking_time = models.PositiveIntegerField(
        'Время приготовления',
        default=1,
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return f'{self.author}, {self.name}'


class Tag(models.Model):
    name = models.CharField(
        'Название тега',
        max_length=255,
        unique=True,
    )
    color = models.CharField(
        'Цветовой HEX-код',
        max_length=7,
        # default='#ffffff',
        null=True,
        blank=True,
        unique=True,
    )
    slug = models.SlugField(
        'Slug тега',
        max_length=255,
        unique=True,
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return f'{self.name}, {self.slug}'


class Ingredient(models.Model):
    name = models.CharField(
        'Название ингредиента',
        max_length=200,
    )
    measurement_unit = models.CharField(
        'Единицы измерения',
        max_length=200
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'
