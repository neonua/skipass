# -*- coding: utf-8 -*-

from django.shortcuts import render
from ..models import Pages

#Cash and delivery page
def cash_and_delivery(request):
    if Pages.objects.filter(title=u'Оплата и доставка'):
        cash = Pages.objects.get(title=u'Оплата и доставка')
    else:
        cash = {'title':u'Страница с именем "Оплата и доставка!',
                      'text':False
                      }
    return render(request, 'cash_and_delivery.html', {'cash':cash})