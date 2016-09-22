# -*- coding: utf-8 -*-

#Import CallBack form
from forms import CallBack


def callback(request): # CallBack form
    form = CallBack()
    return {
        'callback':form,
    }
def cart(request):
    ses = request.session.get('skipass', {})
    request.session['skipass'] = ses
    if 'summ' not in request.session:
        request.session['summ'] = 0
    summ = request.session.get('summ')
    return {'summ':summ, 'ses':ses}



