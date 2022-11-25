<<<<<<< HEAD
from rest_framework.views import APIView
from rest_framework.generics import (
    RetrieveAPIView, ListCreateAPIView,
)

from .models import (
    Exam, ExamTask, ExamParticipant, StudentAnswer, ExamRecord
)
from .serializers import (
    ExamSerializer, ExamTaskSerializer, ExamParicipantSerializer,
    ExamRecordsSerializer, StudentAnswerSerializer
)

'''
    Main Exam Part
'''
class ExamAPIView(ListCreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class ExamDetailAPIView(RetrieveAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

'''
    Exam Task Part
'''

class ExamTaskAPIView(ListCreateAPIView):
    queryset = ExamTask.objects.all()
    serializer_class = ExamTaskSerializer

class ExamTaskDetailAPIView(RetrieveAPIView):
    queryset = ExamTask.objects.all()
    serializer_class = ExamTaskSerializer

"""
    Addition Exam Participant
"""

class ExamTaskAPIView(ListCreateAPIView):
    queryset = ExamTask.objects.all()
    serializer_class = ExamTaskSerializer

class ExamTaskDetailAPIView(RetrieveAPIView):
    queryset = ExamTask.objects.all()
    serializer_class = ExamTaskSerializer

"""
    Exam Participant Addition
"""

class ExamParticipantAdditionAPIView(ListCreateAPIView):
    queryset = ExamParticipant.objects.all()
    serializer_class = ExamParicipantSerializer

class ExamParticipantDetailAPIView(RetrieveAPIView):
    queryset = ExamParticipant.objects.all()
    serializer_class = ExamParicipantSerializer


"""
    Participant Answer Check/Addition
"""

class PartisipantAnswerAPIView(ListCreateAPIView):
    queryset = StudentAnswer.objects.all()
    serializer_class = StudentAnswerSerializer

class PartisipantAnswerDetailAPIView(RetrieveAPIView):
    queryset = StudentAnswer.objects.all()
    serializer_class = StudentAnswerSerializer

"""
    Exam Student Records Check/Addition
"""

class ExamRecordsAPIView(ListCreateAPIView):
    queryset = ExamRecord.objects.all()
    serializer_class = ExamRecordsSerializer

class ExamRecordsSetailAPIView(RetrieveAPIView):
    queryset = ExamRecord.objects.all()
    serializer_class = ExamRecordsSerializer
=======
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
>>>>>>> 6a497cd3f17ff7985cccbe6f4b73022857b10829
