from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    """Описание модели."""
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=100, verbose_name='Описание')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)

    def __str__(self):
        """Строковое представление модели."""
        return self.name


class Product(models.Model):
    """Описание модели."""
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.CharField(max_length=100, verbose_name='Описание')
    preview_image = models.ImageField(upload_to='products/', verbose_name='Изображение(превью)', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за покупку')
    created_at = models.DateField(auto_now=True, verbose_name='дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='дата обновления')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='опубликована')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)
        permissions = [
            ('can_edit_publication_status', 'может отменять публикацию продукта'),
            ('can_edit_description', 'может отменять публикацию продукта'),
            ('can_change_category', 'может менять категорию любого продукта')
        ]

    def __str__(self):
        """Строковое представление модели"""
        return self.name


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    number = models.IntegerField(verbose_name='Номер')
    name = models.CharField(max_length=100, verbose_name='Название')
    is_current = models.BooleanField(verbose_name='Текущая')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
