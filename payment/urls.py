from django.urls import path,include
from .views import success,home

urlpatterns = [
    path('',home,name='home'),
    path('success',success,name='success'),
]
