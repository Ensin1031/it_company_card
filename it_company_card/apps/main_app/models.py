from django.core import validators
from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from uuslug import uuslug


def instance_slug(instance):
    return instance.title


def slugify_value(value):
    return value.replace(' ', '-')


class Promo(models.Model):
    title = models.CharField('Название', max_length=50)
    image = models.ImageField('Фото', upload_to='photos/%Y/%m/%d')
    description = models.TextField('Описание акции', blank=True)
    is_published = models.BooleanField('Опубликовано', default=True)
    show_main = models.BooleanField('Показывать на Главной', default=False)
    discounts = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        verbose_name='Скидка',
        blank=True,
        null=True,
        help_text='От 0.01 до 0.99',
        validators=[validators.MinValueValidator(0.01), validators.MaxValueValidator(0.99)]
    )
    slug = AutoSlugField(
        max_length=100,
        db_index=True,
        unique=True,
        verbose_name='URL Акции',
        populate_from=instance_slug,
        slugify=slugify_value,
    )

    def save(self, *args, **kwargs):
        self.slug = uuslug(self.title, instance=self)
        super(Promo, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('promo', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'
        ordering = ('-discounts',)


