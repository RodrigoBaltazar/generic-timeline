from django.conf import settings
import os
import ffmpy

def converteVideo():
    os.chdir('generictimeline/media/')
    video = os.listdir()
    video_webm = os.path.splitext(video[-1])
    video_webm = video_webm[0] + '.webm'
    ff = ffmpy.FFmpeg(
        inputs={video[-1]: None},
        outputs={video_webm: None}
    )
    ff.run()

converteVideo()