from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Tags', views.Tags, name='index'),
    path('Tags1', views.Tags1, name='index'),
    path('Tags2', views.Tags2, name='index'),
]
