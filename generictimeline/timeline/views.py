from django.shortcuts import render
from django.http import HttpResponse
from .models import Video
from .forms import VideoForm

def timeline(request):
    latest_videos_list = Video.objects.order_by('-pub_date')[:5]
    context = {'latest_videos_list': latest_videos_list,}
    return render(request, 'index.html', context)

def createVideo(request):
    form = VideoForm()
    context = {'form': form}
    return render(request, "timeline/video_form.html", context)