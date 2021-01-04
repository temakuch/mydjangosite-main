from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
			path('',views.show_posts),
			path('/shrek',views.show_shrek ),
			path('post/<int:post_id>', views.show_one_post, name = "one_post"),
			path('register/', views.register)
]