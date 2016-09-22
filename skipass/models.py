# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from tinymce.models import HTMLField
from django.db import models


# Abonement model
class AbonementLow(models.Model):

    class Meta(object):
        verbose_name = u'Скипасс - низкий'
        verbose_name_plural = u'Скипассы - низкий'

    name = models.IntegerField(
        verbose_name=u'Количество дней',
        blank=False
    )

    desc_name = models.CharField(
        verbose_name=u'Дни для отображения',
        max_length=32,
        blank=True
    )

    season = models.ForeignKey(
        'Seasons',
        related_name='season_low',
        verbose_name=u'Cезон',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    price = models.IntegerField(
        verbose_name=u'Цена',
        null=True,
        blank=False
    )

    bukovel_price = models.IntegerField(
        verbose_name=u'В кассах Буковеля',
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if self.season is None:  # Set default reference
            self.season = Seasons.objects.get(name=u'Низкий')
        super(AbonementLow, self).save(*args, **kwargs)

    def __unicode__(self):
        if self.desc_name == '':
            return u'%s' % self.name
        else:
            return u'%s' % self.desc_name

class AbonementHight(models.Model):

    class Meta(object):
        verbose_name = u'Скипасс - высокйи'
        verbose_name_plural = u'Скипассы - высокий'

    name = models.IntegerField(
        verbose_name=u'Количество дней',
        blank=False
    )
    desc_name = models.CharField(
        verbose_name=u'Дни для отображения',
        max_length=32,
        blank=True
    )

    season = models.ForeignKey('Seasons',
        related_name='season_hight',
        verbose_name=u'Cезон',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    price = models.IntegerField(
        verbose_name=u'Цена',
        null=True,
        blank=False
    )

    bukovel_price = models.IntegerField(
        verbose_name=u'В кассах Буковеля',
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if self.season is None:  # Set default reference
            self.season = Seasons.objects.get(name=u'Высокий')
        super(AbonementHight, self).save(*args, **kwargs)

    def __unicode__(self):
        if self.desc_name == '':
            return u'%s' % self.name
        else:
            return u'%s' % self.desc_name

class Seasons(models.Model):

    class Meta(object):
        verbose_name = u'Сезон'
        verbose_name_plural = u'Сезоны'

    name = models.CharField(
        verbose_name=u'Имя сезона',
        max_length=258,
        blank=False
    )

    active = models.CharField(
        verbose_name=u'Активен',
        max_length=256,
        blank=True,
        null=True
    )

    not_active = models.CharField(
        verbose_name=u'Не активен',
        max_length=256,
        blank=True,
        null=True
    )


    def __unicode__(self):
        return u'%s' % self.name

class Promo(models.Model):
    class Meta(object):
        verbose_name = u'Акция'
        verbose_name_plural = u'Акции'

    promo_title = models.CharField(
        verbose_name=u'Заголовок акции',
        max_length=200,
        null=True,
        blank=False
    )

    text = HTMLField(
        verbose_name=u'Текст акции',
        null=True,
        blank=False,
    )

    promo_image = models.ImageField(
        blank=True,
        verbose_name=u"Изображение",
        null=True
    )

    promo_date = models.DateTimeField()

    season = models.ForeignKey('Seasons',

            verbose_name=u'Cезон',
            null=True,
            blank=True,
            on_delete=models.SET_NULL,
            )

    def __unicode__(self):
        return u'%s' % self.promo_title


class ClubCartBuy(models.Model):
    class Meta(object):
        verbose_name = u'Клубные карты'
        verbose_name_plural = u'Клубные карты'

    name = models.CharField(
        verbose_name = u'Имя карты',
        max_length=256,
        null = True,
        blank = False,
    )

    new = models.IntegerField(
        verbose_name = u'Новая',
        null = True,
        blank = False,
    )
    cont = models.IntegerField(
        verbose_name = u'Продление',
        null = True,
        blank = False,
    )

    def __unicode__(self):
        return u'%s' % self.name

class ClubCartBuyDesc(models.Model):
    clubcartbuy = models.ForeignKey(
        ClubCartBuy,
        blank=True,
        null = True,
    )

    desc = models.TextField(
        verbose_name=u'Текст описания',
        blank = True,
        null = False,
    )

    def __unicode__(self):
        return u'%s' % self.clubcartbuy

    class Meta(object):
        verbose_name = u'Описание клубных карт'


class ClubCartPay(models.Model):

    days = models.IntegerField(
        verbose_name=u'Дни',
        blank=True,
        null=False,
    )

    price = models.IntegerField(
        verbose_name = u'Цена',
        blank = True,
        null = False,
    )

    season = models.ForeignKey('Seasons',
        related_name='season',
        verbose_name=u'Cезон',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    def save(self, *args, **kwargs):
        if self.season is None:  # Set default reference
            self.season = Seasons.objects.get(name=u'Высокий')
        super(ClubCartPay, self).save(*args, **kwargs)


    def __unicode__(self):
        return u'Количество дней: %s' % self.days

    class Meta(object):
        verbose_name = u'Пополнение карт'
        verbose_name_plural = u'Пополнение карт'


class QA(models.Model):
    question = models.CharField(
        verbose_name=u'Вопрос',
        max_length=256,
        null= False,
        blank=False
    )

    answer = models.TextField(
        verbose_name=u'Ответ',
        blank=False,
        null=False
    )
    class Meta(object):
        verbose_name = u'Вопросы и ответы'
        verbose_name_plural = u'Вопросы и ответы'
    def __unicode__(self):
        return u'Вопрос: %s' % self.question

class SMTP(models.Model):
    admin_email = models.CharField(
        verbose_name=u'Почтовый адрес администратора',
        blank=False,
        null=False,
        max_length=128,
    )

    host = models.CharField(
        verbose_name=u'адрес SMTP',
        blank=False,
        null=False,
        max_length=128,

    )
    port = models.IntegerField(
        verbose_name=u'Порт',
        blank=False,
        null=False,
    )
    user = models.CharField(
        verbose_name=u'Имя пользователя',
        max_length=128,
        blank=True,
        null=True,
    )
    password = models.CharField(
        verbose_name=u'Пароль',
        max_length=128,
        blank=True,
        null=True
    )
    tls = models.BooleanField(
        verbose_name=u'TLS',
        default=False,
    )
    ssl = models.BooleanField(
        verbose_name=u'SSL',
        default=False,
    )
    class Meta(object):
        verbose_name = u'Настройка почты'
        verbose_name_plural = u'Настройка почты'

    def __unicode__(self):
        return u'SMTP'

class Pages(models.Model):
    title = models.CharField(
        verbose_name=u'Заголовок',
        max_length=200,
        null=True,
        blank=False
    )

    text = HTMLField(
        verbose_name=u'Текст',
        null=True,
        blank=False,

    )

    promo_image = models.ImageField(
        blank=True,
        verbose_name=u"Изображение",
        null=True
    )


    class Meta(object):
        verbose_name = u'Страница'
        verbose_name_plural = u'Страницы'


    def __unicode__(self):
        return u'{}'.format(self.title)