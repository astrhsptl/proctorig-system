import os
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from rest_framework.parsers import (
    FileUploadParser, MultiPartParser
)
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
    Upload Stream
'''

class FileUploadView(APIView):
    parser_classes = [MultiPartParser, FileUploadParser]

    def post(self, request, user=None, format=None):
        file = request.data['multipart']
        default_storage.save(settings.MEDIA_ROOT, ContentFile(file.read()))
        file.close()
        return Response(status=204)

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