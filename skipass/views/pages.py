# -*- coding: utf-8 -*-

from django.shortcuts import render
from ..models import Pages

# Page map
def map(request):
    if Pages.objects.filter(title=u'Карта трасс Буковель'):
        page = Pages.objects.get(title=u'Карта трасс Буковель')
    else:
        page = {'title':u'Страница с именем "Карта трасс Буковель',
                      'text':False
                      }
    return render(request, 'page.html', {'page':page})

#Page weather
def weather(request):
    if Pages.objects.filter(title=u'Погода Буковель'):
        page = Pages.objects.get(title=u'Погода Буковель')
    else:
        page = {'title':u'Страница с именем "Погода Буковель',
                      'text':False
                      }
    return render(request, 'page.html', {'page':page})

#Page cams
def cams(request):
    if Pages.objects.filter(title=u'Веб-камеры'):
        page = Pages.objects.get(title=u'Веб-камеры')
    else:
        page = {'title':u'Страница с именем "Веб-камеры',
                      'text':False
                      }
    return render(request, 'page.html', {'page':page})