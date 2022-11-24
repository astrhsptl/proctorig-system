from django.contrib import admin
from .models import (
    Exam, ExamRecord, ExamTask, ExamParticipant, 
    StudentAnswer
)

class ExamAdmin(admin.ModelAdmin):
    fields = (
        'id', 'date',
    )
    list_display = (
        'id', 'date',
    )
    search_fields = (
        'id', 'date',
    )
    readonly_fields = (
        'id', 'date',
    )

class RecordsAdmin(admin.ModelAdmin):
    fields = (
        'id', 'path', 'exam'
    )
    list_display = (
        'id', 'path', 'exam'
    )
    search_fields = (
        'id', 'path', 'exam'
    )
    readonly_fields = (
        'id',
    )

class TaskAdmin(admin.ModelAdmin):
    fields = (
        'id', 'title', 'discription', 'photo', 'answer',
    )
    list_display = (
        'id', 'title', 'discription', 'photo', 'answer',
    )
    search_fields = (
        'id', 'title', 'discription',
    )
    readonly_fields = (
        'id',
    )


class ExamParticipantAdmin(admin.ModelAdmin):
    fields = (
        'id', 'exam', 'student'
    )
    list_display = (
        'id', 'exam', 'student'
    )
    search_fields = (
        'id', 'exam', 'student'
    )
    readonly_fields = (
        'id',
    )

class AnswersAdmin(admin.ModelAdmin):
    fields = (
        'id', 'task', 'participant', 'answer',
    )
    list_display = (
        'id', 'task', 'participant',
    )
    search_fields = (
        'id', 'task', 'participant',
    )
    readonly_fields = (
        'id', 'answer',
    )

# Exam Admin panels
admin.site.register(Exam, ExamAdmin)
admin.site.register(ExamTask, TaskAdmin)
admin.site.register(ExamRecord, RecordsAdmin)
admin.site.register(ExamParticipant, ExamParticipantAdmin)

# Result Admin panel
admin.site.register(AnswersAdmin, StudentAnswer)