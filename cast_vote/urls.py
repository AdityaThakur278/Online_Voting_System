from django.urls import path,include
from django.contrib import admin

from cast_vote import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('voting',views.voting,name='voting'),
    path('error',views.error,name='error')
]