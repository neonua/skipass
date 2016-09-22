# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from ..forms import Contact
from ..models import Pages
import json
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.core.mail.backends.smtp import EmailBackend
from ..models import SMTP
from django.http import HttpResponse
from ..forms import CallBack
from django.views.decorators.http import require_http_methods




def contact(request):
    if Pages.objects.filter(title=u'Контакты'):
        contact_qs = Pages.objects.get(title=u'Контакты')
    else:
        contact_qs = {'title':u'Страница с именем "Контакты" не создана!',
                      'text':False
                      }
    if request.method == 'POST' and request.is_ajax():
        form = Contact(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            text = form.cleaned_data['text']

            data = {
                'name': name,
                'email': email,
                'text': text

            }
        t = get_template('contact_email.html')
        html = t.render(data)
        config = SMTP.objects.get(pk=1)
        backend = EmailBackend(host=config.host, port=config.port, use_ssl=config.ssl, use_tls=config.tls, username=config.user, password=config.password)
        mail = EmailMultiAlternatives(u'Контактные данные от {0}'.format(form.cleaned_data['name']), 'text',
                                      'BUKSKIPASS.PP.UA | Контактные данные <{0}>'.format(config.user),
                                      ['{0}'.format(config.user)], connection=backend)
        mail.attach_alternative(html, "text/html")
        ajax = {}
        try:
            mail.send()

        except Exception:
            message = u'Во время отправки возникла проблема. Попробуйте заказать позже или свяжитесь с нашим менеджером.'

        else:

            message = u'Спасибо за обращение!'
            ajax['message'] = message
            return HttpResponse(json.dumps(ajax), content_type='application/json')

    else:
        form = Contact()
    return render(request, 'contact.html', {'contact':contact_qs,'form':form})

@require_http_methods(["POST"])
def callback(request):
    if request.method == 'POST' and request.is_ajax():
        form = CallBack(request.POST)
        if form.is_valid():
            ajax={}
            phone = form.cleaned_data['phone']
            name = form.cleaned_data['name']
            data = {'name': name,
                    'phone': phone,
                    }
            t = get_template('callback.html')
            html = t.render(data)
            config = SMTP.objects.get(pk=1)
            backend = EmailBackend(host=config.host, port=config.port, use_ssl=config.ssl, use_tls=config.tls,
                                   username=config.user, password=config.password)
            mail = EmailMultiAlternatives(u'Хотят чтобы вы перезвонили: {0}'.format(form.cleaned_data['name']), 'text',
                                          'BUKSKIPASS.PP.UA | Перезвон <{0}>'.format(config.user),
                                          ['{0}'.format(config.user)], connection=backend)
            mail.attach_alternative(html, "text/html")

            try:
                mail.send()

            except Exception:
                message = u'Во время отправки возникла проблема. Попробуйте заказать позже или свяжитесь с нашим менеджером.'
                ajax['message'] = message
                return HttpResponse(json.dumps(ajax), content_type='application/json')
            else:
                message = u'Спасибо что выбираете нас!. Мы скоро с вами свяжемся ;)'
                ajax['message'] = message
                return HttpResponse(json.dumps(ajax), content_type='application/json')