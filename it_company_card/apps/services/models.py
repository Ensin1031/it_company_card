from django.core import validators
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from django.urls import reverse
from autoslug import AutoSlugField
from uuslug import uuslug

from apps.main_app.models import Promo


def instance_slug(instance):
    return instance.title


def slugify_value(value):
    return value.replace(' ', '-')


class Category(MPTTModel):
    """Модель категорий"""
    title = models.CharField(max_length=50, unique=True, verbose_name='Категория')
    parent = TreeForeignKey(
            'self',
            on_delete=models.CASCADE,
            null=True, blank=True,
            related_name='child_category',
            verbose_name='Назначьте родительскую категорию'
    )
    presence = models.BooleanField(
            default=False,
            verbose_name='Наличие'
    )
    photo = models.ImageField(
            upload_to='photos/%Y/%m/%d',
            blank=True,
            null=True,
            verbose_name='Фото'
    )
    slug = AutoSlugField(
            max_length=100,
            db_index=True,
            unique=True,
            verbose_name='URL Категории',
            populate_from=instance_slug,
            slugify=slugify_value
    )

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('services_by_category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ('title',)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('title',)


class Services(models.Model):
    """
    Model GalleryDB to save new goods to database
    """

    title = models.CharField('Наименование', max_length=100)
    category = TreeForeignKey(
            Category,
            on_delete=models.PROTECT,
            related_name='category_good',
            verbose_name='Категория'
    )
    photo = models.ImageField('Фото', upload_to='photos/%Y/%m/%d')
    description = models.TextField('Описание услуги', blank=True)
    specifications = models.TextField('Характеристики', blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, default=0)
    presence = models.BooleanField('Наличие', default=True)
    n_views = models.IntegerField('Количество просмотров', default=0)
    show_main = models.BooleanField('Показывать на Главной', default=False)
    discounts = models.ForeignKey(
        Promo,
        verbose_name='Скидка по акции',
        on_delete=models.PROTECT,
        related_name='promo_serv',
        null=True,
        blank=True,
    )
    slug = AutoSlugField(
            max_length=255,
            db_index=True,
            unique=True,
            verbose_name='URL Товара',
            populate_from=instance_slug,
            slugify=slugify_value
    )

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self)
        super(Services, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('service', kwargs={'slug': self.slug})

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ('title',)
