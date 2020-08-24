from django.contrib import admin
from django.urls import path
from medcare import views

urlpatterns = [
  
    path('',views.fill_data,name='fill_data'),
    path('add',views.add,name='add'),

]
