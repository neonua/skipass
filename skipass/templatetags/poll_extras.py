# -*- coding: utf-8 -*-
from django import template
from skipass.models import AbonementLow, AbonementHight, Seasons, ClubCartBuy, ClubCartPay

register = template.Library()

@register.filter(name='id')
def id(value):
    value = value.split("_")
    val1 = int(value[0])
    return val1



@register.filter(name='skip')
def skip(value):
    value = value.split("_")
    val1 = int(value[0])

    val2 = value[1]

    if val2 == 'slow':
        name = u'Низкий'
        day = (AbonementLow.objects.get(id=val1).name)
        vtype = u'Скипасс'
    elif val2 == 'shight':
        name = u'Высокий'
        day = (AbonementHight.objects.get(id=val1).desc_name)
        vtype = u'Скипасс'
    elif val2 == 'clubcart':
        name = u'Высокий'
        day = ClubCartPay.objects.get(id=val1).days
        vtype = u'Пополнение карты'
    elif val2 == 'cartnew':
        name = u'Новая карта'
        day = ClubCartBuy.objects.get(id=val1).name
        vtype = u'Клубная карта'
    elif val2 == 'cartcont':
        name = u'Продление'
        day = ClubCartBuy.objects.get(id=val1).name
        vtype = u'Клубная карта'

    def days_skip(val):
        if val == 0:
            day = u'дней'
        elif val % 10 == 1 and value != 11:
            day = u'день'
        elif val % 10 in range(2, 4 + 1):
            day = u'дня'
        else:
            day = u'дней'
        return u"{0} {1}".format(val, day)

    try:
        day = int(day)
    except ValueError:
        day = day

    finally:
        if isinstance(day, int):

            days = days_skip(int(day))
        else:
            days = day
    return u'{2}, {0} ({1})'.format(days, name, vtype)




@register.filter(name='price_one')
def price_one(value):
    value = value.split("_")
    val1 = int(value[0])
    val2 = value[1]

    if val2 =='slow':
        prc = AbonementLow.objects.get(id=val1).price
    elif val2 == 'shight':
        prc = AbonementHight.objects.get(id=val1).price
    elif val2 == 'clubcart':
        prc = ClubCartPay.objects.get(id=val1).price
    elif val2 == 'cartnew':
        prc = ClubCartBuy.objects.get(id=val1).new
    elif val2 == 'cartcont':
        prc = ClubCartBuy.objects.get(id=val1).cont

    return prc

@register.filter(name='price')
def price(value, count):
    value = value.split("_")
    val1 = int(value[0])

    val2 = value[1]
    if val2 == 'slow':
        prc = AbonementLow.objects.get(id=val1).price
    elif val2 == 'shight':
        prc = AbonementHight.objects.get(id=val1).price
    elif val2 == 'clubcart':
        prc = ClubCartPay.objects.get(id=val1).price
    elif val2 == 'cartnew':
        prc = ClubCartBuy.objects.get(id=val1).new
    elif val2 == 'cartcont':
        prc = ClubCartBuy.objects.get(id=val1).cont

    sum_p = prc * count
    return sum_p

@register.filter(name='sum')
def sum(value, count):
    s = price
    sum_p = s * count
    return sum_p

@register.filter(name='count_cart')
def count_cart(value):
    if value == 0:
        name = u'Корзина пустая'
        return u"{0}".format( name)

    elif value%10 == 1:
        name = u'товар'
    elif value%10 in range(2,4+1):
        name = u'товара'
    else:
        name = u'товаров'
    return u"{0} {1}".format(value, name)

@register.filter(name='days')
def days(value):
    if value == 0:
        day = u'дней'
    elif value%10 == 1 and value != 11:
        day = u'день'
    elif value%10 in range(2,4+1):
        day = u'дня'
    else:
        day = u'дней'
    return u"{0} {1}".format(value, day)

@register.filter(name='days_desc')
def days_desc(value):
    day = u'дней'
    return u"{0} {1}".format(value, day)