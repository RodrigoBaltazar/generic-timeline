from django.urls import path
from . import views

urlpatterns = [
    path('', views.timeline, name='timeline'),

    path('create-video/', views.createVideo, name='create-video'),
]