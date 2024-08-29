from django.db import models
from medications.models import Medication


class Reminder(models.Model):
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    reminder_time = models.TimeField()
    message = models.TextField()
    sent = models.BooleanField(default=False)

    def __str__(self):
        return f"Reminder to {self.medication.name} at {self.reminder_time}"
