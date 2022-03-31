from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    path("register_user", views.register_user, name="register_user"),
    path("login_user", views.login_user, name="login_user"),
    path("logout_user", views.logout_user, name="logout_user")
]