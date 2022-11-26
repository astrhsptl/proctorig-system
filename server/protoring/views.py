import os
import cv2
import numpy as np
from PIL import Image
from datetime import datetime
from rest_framework.generics import (
    RetrieveAPIView, ListCreateAPIView,
)
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework import views
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

from .models import ErrorReport
from .serializers import ErrorSerializer
from .analyzator import face, compare_face
from authsystem.models import User, Photos

class FileUploadView(views.APIView):
    parser_classes = [MultiPartParser, FileUploadParser]

    def post(self, request, format=None):
        file = request.data['multipart']
        username = request.data['user']
        path = os.path.join(settings.MEDIA_ROOT, username)

        try:
            os.mkdir(path)
        except:
            print('LOGGED!')
        

        now = str(datetime.today().strftime('%Y-%m-%d'))
        path = os.path.join(path, now)

        try:
            os.mkdir(path)
        except:
            print('LOGGED!')

        try:
            userObj = User.objects.get(username=username)
            photos = Photos.objects.filter(user=userObj)
        except:
            print('User doesnt exist')

        default_storage.save(os.path.join(path, str(file)), ContentFile(file.read()))
        path = os.path.join(path, str(file))

        for i in photos:
            vid = cv2.VideoCapture(path)
            _, image = vid.read()
            cv2.imwrite(os.path.join(os.path.join(settings.MEDIA_ROOT, username), 'scr.png'), image)
            compared = compare_face(os.path.join(os.path.join(settings.MEDIA_ROOT, username), 'scr.png'), os.path.join(settings.MEDIA_ROOT, str(i.path)))
            if not compared: 
                report = ErrorReport.objects.create(student=userObj, discription='Dont match with photo')
                report.save()
                break

        file.close()
        
        faces = face(path)

        if faces != 1:
            report = ErrorReport.objects.create(student=userObj, discription='Dont match with photo')
            report.save()

        return Response(status=204)


class ReportAPIView(ListCreateAPIView):
    queryset = ErrorReport.objects.all()
    serializer_class = ErrorSerializer

class ReportDetailAPIView(RetrieveAPIView):
    queryset = ErrorReport.objects.all()
    serializer_class = ErrorSerializer
