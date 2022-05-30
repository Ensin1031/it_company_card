from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from autoslug import AutoSlugField
from uuslug import uuslug


def instance_slug(instance):
    return instance.title


def slugify_value(value):
    return value.replace(' ', '-')


class Reviews(models.Model):
    """Модель отзывов"""
    OPU = 'OP'
    NMO = 'MN'
    OTK = 'OT'
    REVIEWS_CHOICES = {
        (OPU, 'Опубликован'),
        (NMO, 'На модерации'),
        (OTK, 'Отклонен'),
    }
    title = models.CharField('Название', max_length=50)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        verbose_name='Пользователь',
        related_name='review_user_name',
        null=True,
    )
    date_create = models.DateTimeField('Дата создания отзыва', auto_now_add=True)
    description = models.TextField('Описание товара', blank=True, max_length=300)
    status = models.CharField('Статус отзыва', max_length=2, choices=REVIEWS_CHOICES, default=NMO)
    deleted = models.BooleanField('На удаление', default=False)
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
        super(Reviews, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-date_create',)
