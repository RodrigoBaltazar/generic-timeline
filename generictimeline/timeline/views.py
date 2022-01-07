from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Video
from .forms import VideoForm
from django.core.files.storage import FileSystemStorage
import subprocess, os

def timeline(request):
    latest_videos_list = Video.objects.order_by('-pub_date')[:5]
    context = {'latest_videos_list': latest_videos_list,}
    return render(request, 'index.html', context)

def createVideo(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('timeline')
    else:
        form = VideoForm()
    context = {'form': form}
    return render(request, "timeline/video_form.html", context)