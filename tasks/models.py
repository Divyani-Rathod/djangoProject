from turtle import title
from django.db import models

# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    creared = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title