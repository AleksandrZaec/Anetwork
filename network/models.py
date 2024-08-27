from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class Network(models.Model):
    """
    Модель звена сети
    """

    LEVEL = (
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель')
    )

    name = models.CharField(max_length=35, verbose_name='Название')
    email = models.EmailField(max_length=50, verbose_name='Почта')
    country = models.CharField(max_length=35, verbose_name='Страна')
    city = models.CharField(max_length=35, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Дом')
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, related_name='Покупатели', verbose_name='Поставщик')
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Задолженность')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Время создания')
    level = models.PositiveSmallIntegerField(choices=LEVEL, default=0, verbose_name='Уровень')

    def __str__(self):
        return f'{self.level} {self.name}'

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Product(models.Model):
    """
    Модель продукта
    """

    name = models.CharField(max_length=35,verbose_name='Наименование продукта')
    model = models.CharField(max_length=35,verbose_name='Модель продукта', **NULLABLE)
    release_date = models.DateField(verbose_name='Дата выпуска', auto_now_add=True, **NULLABLE)
    supplier = models.ForeignKey(Network, related_name='Продукты', on_delete=models.CASCADE, verbose_name='Поставщик')

    def __str__(self):
        return f'{self.name} {self.model}\nПоставщик: {self.supplier}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'