from django.urls import path
from siva import views

urlpatterns=[
    path('no/',views.no,name='no'),
]