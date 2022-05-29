from django.core import validators
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from django.urls import reverse
from autoslug import AutoSlugField
from uuslug import uuslug


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
        return reverse('category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ('title',)

    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории(ий)'
        ordering = ('title',)


class Servises(models.Model):
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
    n_views = models.IntegerField('Количество заказов', default=0)
    discounts = models.DecimalField(
            max_digits=3,
            decimal_places=2,
            verbose_name='Скидка',
            null=True,
            help_text='От 0.01 до 0.99',
            validators=[validators.MinValueValidator(0.01), validators.MaxValueValidator(0.99)]
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
        super(Servises, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('good', kwargs={'slug': self.slug})

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Товар(а)'
        verbose_name_plural = 'Товары(ов)'
        ordering = ('title',)
