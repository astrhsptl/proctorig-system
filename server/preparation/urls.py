from django.urls import path 
from .views import (
    # Main Exam event
    ExamAPIView, ExamDetailAPIView,
    
    # Exam Task
    ExamTaskAPIView, ExamTaskDetailAPIView,

    # Exam Participant
    ExamParticipantAdditionAPIView, ExamParticipantDetailAPIView,

    # Participant Answer
    PartisipantAnswerAPIView, PartisipantAnswerDetailAPIView,

    # Exam Records
    ExamRecordsAPIView, ExamRecordsSetailAPIView,
)

urlpatterns = [


    path('exam/', ExamAPIView.as_view()),
    path('exam/<int:pk>', ExamDetailAPIView.as_view()),

    path('task/', ExamTaskAPIView.as_view()),
    path('task/<int:pk>', ExamTaskDetailAPIView.as_view()),

    path('participant/', ExamParticipantAdditionAPIView.as_view()),
    path('participant/<int:pk>', ExamParticipantDetailAPIView.as_view()),

    path('answer/', PartisipantAnswerAPIView.as_view()),
    path('answer/<int:pk>', PartisipantAnswerDetailAPIView.as_view()),

    path('records/', ExamRecordsAPIView.as_view()),
    path('records/<int:pk>', ExamRecordsSetailAPIView.as_view()),
]
