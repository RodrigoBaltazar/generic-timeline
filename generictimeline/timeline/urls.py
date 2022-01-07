from django.urls import path
from . import views
#just for development proporse
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.timeline, name='timeline'),

    path('create-video/', views.createVideo, name='create-video'),
    path('update-videoPath/<str:pk>/', views.updateVideopath, name='update-videopath'),
]

#just for development proporse
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)