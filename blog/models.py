from django.db import models


NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name ='slug', **NULLABLE)
    content = models.TextField(verbose_name='Cодержимое')
    preview_image = models.ImageField(upload_to='blog/', verbose_name='Изображение(превью)', **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return  self.title


    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
