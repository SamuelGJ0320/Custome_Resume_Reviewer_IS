# cvapp/models.py

from django.db import models

class ImprovedCV(models.Model):
    original_cv = models.TextField()  # Para almacenar el CV original
    vacancy_description = models.TextField()  # Para almacenar la descripción de la vacante
    improved_cv = models.TextField()  # Para almacenar el CV mejorado

    def __str__(self):
        return f"CV mejorado para {self.vacancy_description[:30]}..."
