from django.urls import path
from . import views

urlpatterns = [
	path('', views.my_home, name="my-home"),
	path('profile/', views.users_profile, name='users-profile'),
	path('profiles/<profile_id>', views.profiles_list, name="profiles-list"),
	path('pages/', views.posts_control, name="posts-control"),
	path('pages/<post_id>', views.pages, name="blog-pages"),
	path('edit/', views.update_profile, name='update-profile'),
	path('extra_edit/', views.extra_update_profile, name='extra-update-profile'),
	path('update_page/<post_id>', views.update_page, name='update-page'),
	path('delete_page/<post_id>', views.delete_page, name='delete-page')
]