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

# Cart viewer
def cart(request):
    if request.method == 'POST' and request.is_ajax():
        ses = request.session.get('skipass', {}) # Session skipass - id and count
        request.session['skipass'] = ses
        cart_ajax = {} #create dict from respose ajax dump
        if request.POST['summ']: # if in request is 'summ' - update global session info summ
            request.session['summ'] = int(request.POST['summ'])
        if int(request.POST['count']) > 0: # If request count > 0 - update session id and count
            ses[request.POST['id']] = int(request.POST['count'])
            cart_ajax['id'] = request.POST['id']
            cart_ajax['count'] = request.POST['count']
        else: # If request count <=0 - set count 1
            ses[request.POST['id']] = 1
            cart_ajax['id'] = request.POST['id']
            cart_ajax['count'] = 1
        return HttpResponse(json.dumps(cart_ajax), content_type='application/json')

    return render(request, 'cart.html', {})

def delall(request): # Delete all sessions data
    del request.session['skipass']
    del request.session['summ']
    return redirect('/')

def delitem(request, id): # Delete item from cart
    ses = request.session.get('skipass', {})
    del ses[id]
    request.session['skipass'] = ses
    dict= {}
    dict['ok'] = 'ok'
    dict['id'] = id
    request.session['summ'] = int(request.POST['summ'])
    return HttpResponse(json.dumps(dict), content_type='application/json')

def checkout(request): # Create order function
    if request.session.get('skipass', {}):
        ses = request.session.get('skipass', {})
        request.session['skipass'] = ses
        summ = request.session.get('summ')
        if request.method == 'POST' and request.is_ajax(): # Check method POST and AJAX-request
            form = Checkout(request.POST) # create form Checkout
            ajax = {} # create dict from respose ajax dump
            if form.is_valid():
                # Filling form-data  to data-dict. Data dict is data for send mail.
                req = form.cleaned_data['req']
                if req is None:
                    req = False
                town = form.cleaned_data['town']
                phone = form.cleaned_data['phone']
                email = form.cleaned_data['email']
                name = form.cleaned_data['name']
                sename = form.cleaned_data['sename']
                data = {'name':name,
                        'sename':sename,
                        'email':email,
                        'phone':phone,
                        'town':town,
                        'req':req,
                        'ses':ses,
                        'summ':summ}
                t = get_template('email.html') # template from email
                html = t.render(data) # Fillind template data-info
                config = SMTP.objects.get(pk=1) # recipe smtp-config from DB
                backend = EmailBackend(host=config.host, port=config.port, use_ssl=config.ssl, use_tls=config.tls, username=config.user, password=config.password) # Set backend email
                mail = EmailMultiAlternatives(u'Оформление заказа от {0}'.format(form.cleaned_data['name']), 'text', 'BUKSKIPASS.PP.UA | Оформление <neonua666@gmail.com>', [form.cleaned_data['email'], '{0}'.format(config.user)], connection=backend)
                mail.attach_alternative(html, "text/html") # Using alternative mail for sending email template
                # Try to send mail
                try:
                    mail.send()
                # If error
                except Exception:
                    message = u'Во время отправки возникла проблема. Попробуйте заказать позже или свяжитесь с нашим менеджером.'
                    ajax['message'] = message
                    return HttpResponse(json.dumps(ajax), content_type='application/json')
                else:
                    del request.session['skipass'] # Clear session
                    del request.session['summ'] # Clear session
                    request.session['success'] = 1 # Create session from redirect to "success link"
                    ajax['message'] = True
                    ajax['window'] = '/success/'
                    return HttpResponse(json.dumps(ajax), content_type='application/json')


        # If request method is GET
        else:
            form = Checkout() # Create form Checkout
        return render(request, 'checkout.html', {'form':form})
    # If session data is null - redirect to home page
    else:
        return redirect('/')

def success_mail(request): # Check out of order. If you create a order - redirect to "success link", else - redirect to home page
    if 'success' in request.session:
        del request.session['success']
        return render(request, 'success_mail.html', {})
    else:
        return redirect('/')