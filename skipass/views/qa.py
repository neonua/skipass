# -*- coding: utf-8 -*-
from django.shortcuts import render
from ..models import QA

# Create your views here.

#Questions and answers page
def qa(request):
    qa = QA.objects.all()
    return render(request, 'qa.html', {"qa":qa})