from django.db import models
from django.core.validators import RegexValidator


class Genre(models.Model):
    """Класс Жанры."""

    name = models.CharField(
        max_length=256,
        verbose_name='Название',
        db_index=True
    )
    slug = models.SlugField(
        max_length=50,
        verbose_name='slug',
        unique=True,
        validators=[RegexValidator(
            regex=r'^[-a-zA-Z0-9_]+$',
            message='Слаг содержит недопустимый символ!'
        )]
    )

    class Mets:
        verbose_name = 'Жанры'
        verbose_name_plural = 'Жанры'
        ordering = ('name',)

    def __str__(self):
        return self.name