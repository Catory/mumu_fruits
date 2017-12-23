from django.conf.urls import url
from appOne import views

urlpatterns = [

    url(r'^home/', views.home, name='home'),

    url(r'^markethandle/(\d+)/(\d+)/(\d+)/', views.markethandle, name='markethandle'),
    url(r'^cart/', views.cart, name='cart'),
    url(r'^carthandle/(\d)/', views.carthandele, name='carthandle'),

    url(r'^mine/', views.mine, name='mine'),
    url(r'^loadregedit/', views.loadregedit, name='loadregedit'),
    url(r'^checkname/', views.checkname, name='checkname'),
    url(r'^checkpwdagain/', views.checkpwdagain, name='checkpwdagain'),
    url(r'^adduser/', views.adduser, name='adduser'),
    url(r'^payment/', views.payment, name='payment'),
    url(r'^chageorderflag/', views.chageorderflag, name='chageorderflag'),

    url(r'^loadlogin/', views.loadlogin, name='loadlogin'),
    url(r'^dologin/', views.dologin, name='dologin'),
    url(r'^checkloginname/', views.checkloginname, name='checkloginname'),
    url(r'^minelogout/', views.minelogout, name='minelogout'),
    url(r'^regeditsuccsess/', views.regeditsuccsess, name='regeditsuccsess'),
    url(r'^orderlist/', views.orderlist, name='orderlist'),
]
