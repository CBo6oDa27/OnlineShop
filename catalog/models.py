from django.db import models

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
    created_at = models.DateField()
    updated_at = models.DateField()
    #manufactured_at = models.DateField(verbose_name='Дата производства продукта', **NULLABLE)


    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('name',)

    def __str__(self):
        """Строковое представление модели"""
        return self.name



