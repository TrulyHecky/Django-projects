from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=75, null=True)
    goal = models.CharField(max_length=200, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name