from django.urls import path
from . import views

app_name = 'education'

urlpatterns = [
    path('', views.home, name='home'),  # Home sahifasi
    path('davomat/qoshish/', views.davomat_qoshish, name='davomat_qoshish'),
    path('uy_ishi/' , views.homework_qoshish, name='homework_qoshish'),
    path('about/' , views.about, name='about'),
]