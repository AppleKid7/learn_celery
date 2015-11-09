from django.db import models
from django.contrib.auth.models import User


class JobModel(models.Model):
    user = models.ForeignKey(User)
    task_id = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.task_id
