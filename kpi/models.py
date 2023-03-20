from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Report(models.Model):
    """Класс сохранения данных"""
    date = models.DateField(default=datetime.now) #TODO is today.now
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    method = models.CharField(max_length=255)
    input_data = models.JSONField(default=dict) #TODO Параметры введеные данные в формате словаря

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.date, self.method
