# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..forms import Checkout
import json
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.core.mail.backends.smtp import EmailBackend
from ..models import SMTP
# Create your views here.


config = SMTP.objects.get(pk=1)
backend = EmailBackend(host=config.host, port=config.port, use_ssl=config.ssl, use_tls=config.tls, username=config.user, password=config.password)


def cart(request):
    ses = request.session.get('skipass', {})
    request.session['skipass'] = ses
    summ = request.session.get('summ')

    if request.method == 'POST' and request.is_ajax(): # if request method is POST and ajax
        cart_ajax = {} # create dict for ajax
        if request.POST['summ']:
            request.session['summ'] = int(request.POST['summ'])
        if int(request.POST['count']) > 0:
            ses[request.POST['id']] = int(request.POST['count'])
            cart_ajax['id'] = request.POST['id']
            cart_ajax['count'] = request.POST['count']
        else:
            ses[request.POST['id']] = 1
            cart_ajax['id'] = request.POST['id']
            cart_ajax['count'] = 1
        return HttpResponse(json.dumps(cart_ajax), content_type='application/json')
    return render(request, 'cart.html', { 'ses':ses, 'summ':summ })

def delall(request):
    del request.session['skipass']
    del request.session['summ']
    return redirect('/')

def delitem(request, id):
    ses = request.session.get('skipass', {})
    del ses[id]
    request.session['skipass'] = ses
    dict= {}
    dict['ok'] = 'ok'
    dict['id'] = id
    request.session['summ'] = int(request.POST['summ'])
    return HttpResponse(json.dumps(dict), content_type='application/json')

def checkout(request):
    if request.session.get('skipass', {}):
        ses = request.session.get('skipass', {})
        request.session['skipass'] = ses
        summ = request.session.get('summ')
        if request.method == 'POST':
            form = Checkout(request.POST)
            if form.is_valid():
                req = form.cleaned_data['req']
                if req is None:
                    req = False
                town = form.cleaned_data['town']
                phone = form.cleaned_data['phone']
                email = form.cleaned_data['email']
                name = form.cleaned_data['name']
                data = {'name':name,
                        'email':email,
                        'phone':phone,
                        'town':town,
                        'req':req,
                        'ses':ses,
                        'summ':summ}
                t = get_template('email.html')
                html = t.render(data)
                mail = EmailMultiAlternatives(u'Оформление заказа от {0}'.format(form.cleaned_data['name']), 'text', 'neonua666@gmail.com', [form.cleaned_data['email'], 'neonua666@gmail.com'], connection=backend)
                mail.attach_alternative(html, "text/html")

                try:
                    mail.send()

                except Exception:
                    message = u'Во время отправки возникла проблема. Попробуйте заказать позже или свяжитесь с нашим менеджером.'

                else:
                    message = u'Заказ успешно передан нашим менеджерам. Скоро с вами свяжемся ;)'
                    return redirect('/delall/')



        else:
            form = Checkout()
        return render(request, 'checkout.html', {'ses':ses, 'summ':summ, 'form':form})
    else:
        return redirect('/')