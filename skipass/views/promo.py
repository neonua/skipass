# -*- coding: utf-8 -*-
from django.shortcuts import render
from ..models import Promo

# Create your views here.

#Promo page
def promo(request):
    promo = Promo.objects.all()
    return render(request, 'promo.html', {'promo':promo})