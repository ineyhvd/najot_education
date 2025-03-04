from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.auth_view, name='auth'),  # Birinchi sahifa login/register
    path('logout/', views.logout_view, name='logout'),
]