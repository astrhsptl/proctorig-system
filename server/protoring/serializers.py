from rest_framework import serializers

from .models import (
    ErrorReport
)


class ErrorSerializer(serializers.ModelSerializer):
    date = serializers.DateField()
    class Meta:
        model = ErrorReport
        fields = "__all__"

