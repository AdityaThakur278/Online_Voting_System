from django.urls import path,include
from django.contrib import admin

from voter_reg import views

urlpatterns = [

    path('registration',views.registration,name='registration')
]