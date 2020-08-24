from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.hey,name='hey'),
    path('subtract',views.subtract,name='subtract')
]
