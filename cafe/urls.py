from django.urls import path,  include
from cafe import views

app_name = 'cafe'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
]