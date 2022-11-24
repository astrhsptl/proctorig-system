from django.db import models
from server.settings import AUTH_USER_MODEL as User


class Exam(models.Model):
    date = models.DateField()

class ExamRecord(models.Model):
    path = models.FileField(upload_to='records/%Y/%m/%d')
    exam = models.ForeignKey(Exam, models.CASCADE)

class ExamTask(models.Model):
    title = models.CharField(max_length=255)
    discription = models.TextField(max_length=4096)
    photo = models.ImageField(upload_to='exam_tasks/%Y/%m/%d', null=True)
    answer = models.CharField(max_length=255)

class Photos(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    path = models.ImageField(upload_to='photos/%Y/%m/%d', blank=False)