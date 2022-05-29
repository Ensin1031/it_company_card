from django.db import models


class Banners(models.Model):
    title = models.CharField('Название', max_length=50)
    image = models.ImageField('Фото', upload_to='photos/%Y/%m/%d')
    is_published = models.BooleanField('Опубликовано', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры на главную'


