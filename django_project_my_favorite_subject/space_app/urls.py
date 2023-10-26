from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.main, name='main'),
    path('space_app/', views.space_app, name='space_app'),
    path('space_app/details/<int:id>', views.details, name='details'),
    path('space_app/staticfiles/image_collection', views.image_collection, name='image_collection'),
]

urlpatterns += staticfiles_urlpatterns()