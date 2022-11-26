from django.urls import path 
from .views import FileUploadView, ReportAPIView, ReportDetailAPIView

urlpatterns = [
    path('upl/', FileUploadView.as_view()),
    
    path('reports/', ReportAPIView.as_view()),
    path('reports/<int:pk>', ReportDetailAPIView.as_view()),
]
