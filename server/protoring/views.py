import os
from django.shortcuts import render
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework import views
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from moviepy.editor import *

def editing():
    videos = os.listdir('/home/nia/Desktop/proctorig-system/server/media')
    if len(videos) >= 2:
        main = VideoFileClip(os.path.join('/home/nia/Desktop/proctorig-system/server/media', videos[0]))
        print(videos[0])
        for i in videos[1:-1]:
            additionClip = VideoFileClip(os.path.join('/home/nia/Desktop/proctorig-system/server/media', i))
            concatnate = concatenate_videoclips([main, additionClip])
            concatnate.write_videofile(os.path.join('/home/nia/Desktop/proctorig-system/server/media', videos[0]))

class FileUploadView(views.APIView):
    parser_classes = [MultiPartParser, FileUploadParser]

    def post(self, request, format=None):
        print('start')
        file = request.data['multipart']
        print(f'{file}, {type(file)}')
        path = default_storage.save(str(request.data['multipart']), ContentFile(file.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        file.close()
        editing()
        print(f'end: {tmp_file}')
        return Response(status=204)