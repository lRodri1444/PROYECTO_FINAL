from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginView ,name='login'),
    path('register/',views.user_registration, name='user-registration'),
    path('about/', views.about_page, name="about-page")
]