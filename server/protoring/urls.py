from django.urls import path 

from .views import (
    # Uploads
    FileUploadView,

)

urlpatterns = [
    # Uploads
    path('upl', FileUploadView.as_view()),
]