from django.urls import path
from . import views

app_name = 'communities'

urlpatterns = [
    path('', views.communities, name="list"),
    path('new-communities', views.communities, name="communities"),
    path('<slug:slug>/', views.communities_page, name="page"),  
]