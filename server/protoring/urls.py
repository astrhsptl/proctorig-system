from django.urls import path 
from .views import FileUploadView


urlpatterns = [
    path('upl', FileUploadView.as_view()),
]
