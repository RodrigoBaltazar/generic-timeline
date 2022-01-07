import os
import subprocess

def converteVideo(video):
    video_origem = '../generictimeline/media/ %s' %(video)
    video_destino = os.path.splitext(video_origem[0])
    video_destino = video_origem + '.webm'
    subprocess.run('ffmpeg -i %s %s' %(video_origem, video_destino))