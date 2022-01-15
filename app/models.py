from django.db import models
from datetime import date


# Create your models here.
class Todo(models.Model):
    text = models.CharField("",max_length=50)
    completed = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    completion_date = models.DateField("Date:",auto_now_add=False,auto_now=False,blank=False)
    
    def __str__(self):
        return self.text

    @property
    def is_past_due(self):
        return date.today() > self.completion_date
    def date_difference(self):
        return date.today() - self.completion_date
