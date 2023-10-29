from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.main, name='main'),
    path('space_app/', views.space_app, name='space_app'),
    path('space_app/details/<int:id>', views.details, name='details'),    
    path('space_app/staticfiles/image_collection', views.image_collection, name='image_collection'),
    path('space_app_post/', views.space_app_post, name='space_app_post'),
    path('space_app_post/details/<int:id>', views.posts_details, name='posts_details'),
]

urlpatterns += staticfiles_urlpatterns()