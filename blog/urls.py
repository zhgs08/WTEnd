from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name="index"),
    path('blogs/', views.blog_list, name="blog_list"),
    path('blogs/create', views.blog_create, name="blog_create"),   
    path('blogs/update/<int:blog_id>', views.blog_update, name="blog_update"),
    path('blogs/delete/<int:blog_id>', views.blog_delete, name="blog_delete"),
]