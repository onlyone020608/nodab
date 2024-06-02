#coplate/urls.py 생성 후 

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]