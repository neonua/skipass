
from django.conf.urls import url
from django.contrib import admin
from skipass.views import skipass, qa, balance, promo, cart, club, contact, cash_and_delivery, pages
from settings import *
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', skipass.skipass, name='skipass'),
    url(r'^delall/$', cart.delall, name='delall'),
    url(r'^del/(?P<id>\S+)/$', cart.delitem),
    url(r'^promo/$', promo.promo, name='promo'),
    url(r'^cart/$', cart.cart, name='cart'),
    url(r'^acart_low/(?P<id>\d+)/$', skipass.acart_low, name='acart_low'),
    url(r'^acart_hight/(?P<id>\d+)/$', skipass.acart_hight, name='acart_hight'),
    url(r'^club_cart/$', club.club_cart, name='club_cart'),
    url(r'^acart_club/(?P<id>\d+)/$', club.acart_club, name='club'),
    url(r'^acart_new/(?P<id>\d+)/$', club.acart_new, name='acart_new'),
    url(r'^acart_cont/(?P<id>\d+)/$', club.acart_cont, name='acart_cont'),
    url(r'^balance/$', balance.balance, name='balance'),
    url(r'^qa/$', qa.qa, name='qa'),
    url(r'^checkout/$', cart.checkout, name='checkout'),
    url(r'^success/$', cart.success_mail),
    url(r'^contact/$', contact.contact),
    url(r'^cash_and_delivery/$', cash_and_delivery.cash_and_delivery),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^form-callback/$', contact.callback),
    url(r'^map/$', pages.map),
    url(r'^weather/$', pages.weather),
    url(r'^cams/$', pages.cams),

]
