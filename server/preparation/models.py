from django.db import models
from authsystem.models import  User


class Exam(models.Model):
    title = models.CharField(max_length=255, unique=True)
    date = models.DateField()

class ExamRecord(models.Model):
    path = models.FileField(upload_to='records/%Y/%m/%d')
    exam = models.ForeignKey(Exam, models.CASCADE, related_name='exam_record')

class ExamTask(models.Model):
    exam = models.ForeignKey(Exam, models.CASCADE,related_name='exam_task')
    title = models.CharField(max_length=255)
    discription = models.TextField(max_length=4096)
    photo = models.ImageField(upload_to='exam_tasks/%Y/%m/%d', null=True)
    answer = models.CharField(max_length=255)

class ExamParticipant(models.Model):
    exam = models.ForeignKey(Exam, models.CASCADE,related_name='exam_participant')
    student = models.ForeignKey(User, models.CASCADE)

class StudentAnswer(models.Model):
    task = models.ForeignKey(ExamTask, models.CASCADE)
    participant = models.ForeignKey(ExamParticipant, models.CASCADE)
    answer = models.CharField(max_length=255)