"""siteprodaja URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from mebel import views
from mainpage import views as v
from mainpage.views import YandexNotifications as yy
urlpatterns = [
    path('admin/', admin.site.urls),
    path('mebels/',views.mebels,name='mebels'),
    path('mebels/', include('mebel.urls')),
    path('',v.homepage,name='home'),
    path('korzina/',v.korzina,name='korzina'),
    path('oplata/',v.oplata,name='oplata'),
    path('otmena/',v.otmena,name='otmena'),
    path('novinki/',views.novinki,name='novinki'),
    path('notifications/',yy.post,name='notifications'),
    path('novinki/',views.novinki,name='novinki'),
    path('photo/',v.photo,name='photo'),
    path('nravit/',v.nravit,name='nravit'),
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)