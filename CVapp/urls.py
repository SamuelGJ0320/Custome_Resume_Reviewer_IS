# CVapp/urls.py
from django.urls import path
from .views import custom_resume_view

urlpatterns = [
    path('', custom_resume_view, name='custom_resume_view'),
]