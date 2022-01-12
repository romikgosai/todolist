from django.db import models
from datetime import date


# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    completion_date = models.DateField("Completion Date:(mm/dd/yyyy)",auto_now_add=False,auto_now=False,blank=True)

    def __str__(self):
        return self.text

    