from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from uuslug import uuslug


def instance_slug(instance):
    return instance.title


def slugify_value(value):
    return value.replace(' ', '-')


class News(models.Model):
    title = models.CharField('Название', max_length=150)
    content = models.TextField('Контент', max_length=1000, blank=True)
    date_create = models.DateTimeField('Дата создания записи', auto_now_add=True)
    is_published = models.BooleanField('Опубликовано', default=True)
    image = models.ImageField('Фото', upload_to='photos/%Y/%m/%d')
    slug = AutoSlugField(
        'Url записи',
        max_length=150,
        db_index=True,
        unique=True,
        populate_from=instance_slug,
        slugify=slugify_value,
    )

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self)
        super(News, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ('-date_create',)
