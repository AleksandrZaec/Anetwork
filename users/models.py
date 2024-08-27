from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """
    Модель пользователя
    """
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=15, unique=True, verbose_name='Телефон', **NULLABLE)
    country = models.CharField(max_length=15, verbose_name='Страна', **NULLABLE)
    city = models.CharField(max_length=15, verbose_name='Город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/avatar/', verbose_name='Аватар', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email