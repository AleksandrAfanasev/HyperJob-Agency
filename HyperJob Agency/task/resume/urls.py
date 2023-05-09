from django.urls import path
from .views import *


urlpatterns = [
    path('resumes/', ResumeView.as_view()),
    path('resume/new', NewResumeView.as_view()),
]

