from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('shortener/', views.url_short, name='shortener'),
    path('logout/', views.logout_user, name="logout"),
    path('list/', views.list_shortener, name='list'),
]
