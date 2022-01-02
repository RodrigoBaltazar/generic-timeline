from django.shortcuts import render
from django.http import HttpResponse
from .models import Video

def timeline(request):
    timeline = Video.objects.all()
    context = {'timeline': timeline}
    return render(request, 'timeline/index.html', context)