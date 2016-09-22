# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..models import AbonementLow, AbonementHight, Seasons
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import json
from django.shortcuts import get_object_or_404

# Create your views here.

def skipass(request):
    abonem_low = AbonementLow.objects.all()
    abonem_hight = AbonementHight.objects.all()
    seasons = Seasons.objects.all()
    abonem_low = abonem_low.order_by('name')
    abonem_hight = abonem_hight.order_by('name')
    ses = request.session.get('skipass', {})
    request.session['skipass'] = ses
    if 'summ' not in request.session:
        request.session['summ'] = 0
    summ = request.session.get('summ')

    return render(request, 'index.html', {'abonements_low':abonem_low, 'abonements_hight':abonem_hight,'seasons':seasons, 'ses':ses, 'summ':summ})


def acart_low(request, id):
    obj_low = get_object_or_404(AbonementLow, id=id)
    id_ses = str(id + "_" + 'slow')
    ses = request.session.get('skipass', {})
    cnt = 1
    price = obj_low.price
    if id_ses not in ses:
        cnt = cnt
        ses[id_ses] = cnt
        request.session['summ'] += price
    elif id_ses in ses:
        ses[id_ses] +=cnt
        request.session['summ'] += price * cnt
    request.session['skipass'] = ses
    return redirect('/cart/')

def acart_hight(request, id):
    obj_hight = get_object_or_404(AbonementHight, id=id)
    id_ses = str(id + "_" + 'shight')
    ses = request.session.get('skipass', {})
    cnt = 1
    price = obj_hight.price
    if id_ses not in ses:
        cnt = cnt
        ses[id_ses] = cnt
        request.session['summ'] += price
    elif id_ses in ses:
        ses[id_ses] += cnt
        request.session['summ'] += price * cnt
    request.session['skipass'] = ses
    return redirect('/cart/')
