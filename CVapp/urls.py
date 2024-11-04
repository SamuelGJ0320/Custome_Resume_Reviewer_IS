from django.urls import path
from . import views

urlpatterns = [
    path('', views.custom_resume_view, name='custom_resume_view'),
    path('fetch_recommendations/', views.fetch_recommendations, name='fetch_recommendations'),
]
