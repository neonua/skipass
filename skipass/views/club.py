# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from ..models import Seasons, ClubCartPay, ClubCartBuy
from django.shortcuts import get_object_or_404

# Create your views here.


def club_cart(request):
    pay = ClubCartPay.objects.all()
    buy = ClubCartBuy.objects.all()
    seasons = Seasons.objects.all()
    ses = request.session.get('skipass', {})
    request.session['skipass'] = ses
    if 'summ' not in request.session:
        request.session['summ'] = 0
    summ = request.session.get('summ')

    return render(request, 'club.html', {'pay':pay, 'buy':buy, 'seasons':seasons, 'ses':ses, 'summ':summ})

def acart_club(request, id):
    club = get_object_or_404(ClubCartPay, id=id)
    id_ses = str(id + "_" + "clubcart")
    ses = request.session.get('skipass', {})
    cnt = 1
    if id_ses not in ses:
        cnt = cnt
        ses[id_ses] = cnt
        request.session['summ'] += club.price
    elif id_ses in ses:
        ses[id_ses] += cnt
        request.session['summ'] += club.price * cnt
    request.session['skipass'] = ses
    return redirect('/cart/')

def acart_new(request, id):
    new = get_object_or_404(ClubCartBuy, id=id)
    id_ses = str(id + "_" + "cartnew")
    ses = request.session.get('skipass', {})
    cnt = 1
    if id_ses not in ses:
        cnt = cnt
        ses[id_ses] = cnt
        request.session['summ'] += new.new
    elif id_ses in ses:
        ses[id_ses] += cnt
        request.session['summ'] += new.new * cnt
    request.session['skipass'] = ses
    return redirect('/cart/')

def acart_cont(request, id):
    cont = get_object_or_404(ClubCartBuy, id=id)
    id_ses = str(id + "_" + "cartcont")
    ses = request.session.get('skipass', {})
    cnt = 1
    if id_ses not in ses:
        cnt = cnt
        ses[id_ses] = cnt
        request.session['summ'] += cont.cont
    elif id_ses in ses:
        ses[id_ses] += cnt
        request.session['summ'] += cont.cont * cnt
    request.session['skipass'] = ses
    return redirect('/cart/')