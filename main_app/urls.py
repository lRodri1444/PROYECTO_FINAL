from django.urls import path
from . import views

urlpatterns = [
	path('', views.my_home, name="my-home"),
	path('profile/', views.users_profile, name='users-profile'),
	path('edit/', views.update_profile, name='update-profile'),
	path('extra_edit/', views.extra_update_profile, name='extra-update-profile')
]