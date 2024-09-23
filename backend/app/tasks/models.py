from django.db import models 

class Task(models.Model):
    title = models.CharField(blank=False, max_length=40)
    body = models.TextField(blank=False)

    def __str__(self):
        return f"pk:{self.pk}-{self.title}"