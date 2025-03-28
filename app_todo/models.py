from django.db import models


# Create your models here.
class Task_class(models.Model):
    task_text=models.CharField(max_length=999)
    is_it_done=models.BooleanField()
    def __str__(self):
        return self.task_text
