from rest_framework.generics import (
    RetrieveAPIView, ListCreateAPIView, ListAPIView
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

class ExamDetailAPIView(ListAPIView):
    queryset = ExamTask.objects.raw('select id, exam_id, title from preparation_examtask')
    serializer_class = ExamTaskSerializer

    def get_queryset(self):
        return ExamTask.objects.raw(f'''
        select id, exam_id, title from preparation_examtask where exam_id={self.kwargs['pk']};
        ''')

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