# -*- coding: utf-8 -*-

from django import forms
from tinymce.widgets import TinyMCE
from django.contrib import admin
from .models import AbonementLow, AbonementHight, Seasons, Promo, ClubCartBuy, ClubCartBuyDesc, ClubCartPay, QA, SMTP, Pages
# Register your models here.

class ClubCartBuyDescInline(admin.TabularInline):
    model = ClubCartBuyDesc
    fieldsets = (
        (
            None,
            {
                'fields': ('desc',)
            }
        ),
    )
    extra = 0

class ClubCartBuyModel(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {
                'fields': ('name', 'new', 'cont',)
            }
        ),
    )
    inlines = (ClubCartBuyDescInline,)
    list_display = ['name', 'new', 'cont']


class SMTPAdmin(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):  # note the obj=None
            return False
    def has_add_permission(self, request, obj=None):
        if SMTP.objects.all():
            return False
        else:
            return True


class AbonementLowAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc_name', 'price',]
    exclude = ['season']

class ClubCartBuyAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {
                'fields': ('days', 'price')
            }
        ),
    )
    list_display = ['days', 'price']
    exclude = ['season']

class TextForm(forms.ModelForm):
    text = forms.CharField(widget=TinyMCE(attrs={'cols': 120, 'rows': 30}))
    model = Promo

class PagesForm(forms.ModelForm):
    text = forms.CharField(widget=TinyMCE(attrs={'cols': 120, 'rows': 30}))
    model = Pages

class PromoAdmin(admin.ModelAdmin):
    form = TextForm

class PagesAdmin(admin.ModelAdmin):
    form = PagesForm


admin.site.register(AbonementLow, AbonementLowAdmin)
admin.site.register(AbonementHight, AbonementLowAdmin)
admin.site.register(Seasons)
admin.site.register(Promo, PromoAdmin)
admin.site.register(ClubCartBuy, ClubCartBuyModel)
admin.site.register(ClubCartPay, ClubCartBuyAdmin)
admin.site.register(QA)
admin.site.register(SMTP, SMTPAdmin)
admin.site.register(Pages, PagesAdmin)
