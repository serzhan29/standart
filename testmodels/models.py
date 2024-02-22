from django.db import models
from django.contrib.auth.models import User


class TestModel(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
