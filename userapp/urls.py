from django.urls import path
from userapp import views

urlpatterns=[
    path('username' , views.username)
]