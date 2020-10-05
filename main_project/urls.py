from django.urls import path,include
from django.contrib import admin

from main_project import views

urlpatterns = [
    path('main_page',views.main_page,name='main_page')
]