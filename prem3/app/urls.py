from django.urls import path
from app import views

urlpatterns=[
    path('display/',views.display,name='display')
]