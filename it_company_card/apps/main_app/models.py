from django.core import validators
from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from autoslug import AutoSlugField
from uuslug import uuslug
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError


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


class Contacts(models.Model):
    name = models.CharField('Имя', max_length=100)
    content = models.TextField('Текст сообщения', max_length=1000)
    email_user = models.EmailField('E-mail', help_text='введите ваш E-mail')
    phone = PhoneNumberField('Номер телефона')
    reviewed = models.BooleanField('Рассмотрено', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ('name',)


@receiver(post_save, sender=Contacts)
def sign_for_save_post_contacts(sender, instance, created, **kwargs):
    admin_list = User.objects.filter(is_superuser=True)
    admin_email_list = []
    for email in admin_list:
        admin_email_list.append(email.email)
    subject = 'Тест сайт'
    message = f'New message from {instance}, {instance.email_user} '
    for admin in admin_email_list:
        send_mail(subject, message, 'ensin81@mail.ru', (admin,), fail_silently=False)
    return admin_list


