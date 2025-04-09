from django.db import models


# Create your models here.
class Task_class(models.Model):
    task_text=models.CharField(max_length=999)
    is_it_done=models.BooleanField()
    def __str__(self):
        return self.task_text

class Themepicker(models.Model):
    is_it_black=models.BooleanField()
    tag=models.CharField(max_length=5, default="tag")
    def __str__(self):
        return self.is_it_black