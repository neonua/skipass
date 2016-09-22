# -*- coding: utf-8 -*-
from django import forms


class CallBack(forms.Form):
    name = forms.CharField(
        label=u'Контактное лицо',
        max_length=128,
        widget=forms.TextInput(
            attrs={'placeholder': 'Как к вам можно обращаться?',
                   'class': 'form-control',
                   'required': True,
                   })
    )

    phone = forms.CharField(
        label=u'Номер телефона',
        max_length=13,
        widget=forms.TextInput(
            attrs={'placeholder': '+380961234567',
                   'class': 'form-control',
                   'required': True,
                   'pattern': '^[+]?[0-9,\-,(,),\s]{6,20}$',
                   'title': u'+380961234567',
                   })

    )

class Contact(forms.Form):
    name = forms.CharField(
        label=u'Контактное лицо',
        max_length=128,
        widget=forms.TextInput(
            attrs={'placeholder': 'Контактное лицо',
                   'class': 'form-control',
                   'required': True,
                   })

    )

    email = forms.EmailField(
        label=u'Email',
        widget=forms.TextInput(
            attrs={'placeholder': 'sample@examle.com',
                   'class': 'form-control',
                   'required': True,
                   'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$',
                   'title': u'sample@example.com'
                   })
    )

    text = forms.CharField(
        label=u'Сообщение',
        widget=forms.Textarea(
            attrs={
                   'class': 'form-control',
                   'required': True,
                   })
        )




class Checkout(forms.Form):
    name = forms.CharField(
        label=u'Имя',
        max_length=128,
        widget=forms.TextInput(
            attrs={'placeholder': 'Игорь',
                   'class':'form-control',
                   'required': True,
                   'pattern': '[A-Za-zА-Яа-яЁёІіЇїҐґ]{2,}',
                    'title': u'Нужно ввести не менее двух букв',
                   })

    )

    sename = forms.CharField(
        label=u'Фамилия',
        max_length=128,
        widget=forms.TextInput(
            attrs={'placeholder': 'Семенюк',
                   'class': 'form-control',
                   'required': True,
                   'pattern': '[A-Za-zА-Яа-яЁёІіЇїҐґ]{2,}',
                   'title': u'Нужно ввести не менее двух букв',
                   })

    )

    email = forms.EmailField(
        label=u'Email',
        widget=forms.TextInput(
            attrs={'placeholder': 'sample@examle.com',
                   'class':'form-control',
                   'required': True,
                   'pattern':'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$',
                   'title': u'sample@example.com'
                   })
    )

    phone = forms.CharField(
        label=u'Номер телефона',
        max_length=13,
        widget=forms.TextInput(
            attrs={'placeholder': '+380961234567',
                   'class':'form-control',
                   'required': True,
                   'pattern':'^[+]?[0-9,\-,(,),\s]{6,20}$',
                   'title': u'+380961234567',
                   })

    )

    town = forms.CharField(
        label=u'Город',
        max_length=u'64',
        widget = forms.TextInput(
            attrs={'placeholder': 'Киев',
                   'class':'form-control',
                   'required': True,
                   'pattern': '^[A-Za-zА-Яа-яЁёІіЇїҐґ]+$',
                   })
    )

    req = forms.CharField(
        label=u'Отделение новой почты',
        max_length=128,
        widget=forms.TextInput(attrs={'placeholder': '1', 'class':'form-control', 'required': False}),
        required = False,

    )



