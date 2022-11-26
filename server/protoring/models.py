from django.db import models
from authsystem.models import User


class ErrorReport(models.Model):
    discription = models.CharField(max_length=255)
    student = models.ForeignKey(User, models.CASCADE)
    date = models.DateField(auto_now_add=True)