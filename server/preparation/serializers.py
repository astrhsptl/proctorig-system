from rest_framework import serializers

from .models import (
    Exam, ExamTask, ExamParticipant, StudentAnswer, ExamRecord
)


class ExamSerializer(serializers.ModelSerializer):
    date = serializers.DateField()
    class Meta:
        model = Exam
        fields = ('id', 'title', 'date',)
    
class ExamTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamTask
        fields = ('id', 'exam', 'title', 'discription', 'photo', 'answer')

class ExamParicipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamParticipant
        fields = ('id', 'exam', 'student',)

class StudentAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAnswer
        fields = ('id', 'task', 'participant', 'answer')
    
class ExamRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamRecord
        fields = ('id', 'path', 'exam')