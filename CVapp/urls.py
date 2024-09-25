# CVapp/urls.py
from django.urls import path
from .views import custom_resume_view  # Importa directamente desde views

urlpatterns = [
    path('', custom_resume_view, name='custome_resume'),  # nombre de mi archivo html 
]
