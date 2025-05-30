from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('authorize/', views.authorize, name='authorize'),
    path('oauth2callback/', views.oauth2callback, name='oauth2callback'),
]
