from django.urls import path, include
from . import views

app_name='blog'
urlpatterns = [
    path('crovati/',views.crovati,name='crovati'),
    path('stulia/',views.stulia,name='stulia'),
    path('stoli/',views.stoli,name='stoli'),
    path('barnie_stulya/',views.barnie_stulya,name='barnie_stulya'),
    path('cresla/',views.cresla,name='cresla'),
    path('divani/',views.divani,name='divani'),
    
    path('bar/<int:blog_id>',views.detail_barstul,name='detail_barstul'),
    path('stul/<int:blog_id>',views.detail_stul,name='detail_stul'),
    path('stol/<int:blog_id>',views.detail_stol,name='detail_stol'),
    path('div/<int:blog_id>',views.detail_div,name='detail_div'),
    path('cres/<int:blog_id>',views.detail_cres,name='detail_cres'),
    path('crov/<int:blog_id>',views.detail_crov,name='detail_crov'),
    
]