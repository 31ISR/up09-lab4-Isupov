
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('', views.index),
    path('posts/', include('posts.urls')),
    path('communities/', include('communities.urls')),
]
