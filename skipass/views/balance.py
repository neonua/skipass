# -*- coding: utf-8 -*-
from django.shortcuts import render


# Create your views here.

def balance(request):  #Check balance of skipass

    return render(request, 'balance.html', {})