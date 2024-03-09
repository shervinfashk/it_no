from django.db import models

# Create your models here.

class Post(models.Model):
    TITLE = models.CharField(max_length=100)
    HANDLE = models.CharField(max_length=100)
    QTY = models.IntegerField()
    PRICE = models.IntegerField()
    IMAGE = models.TextField()
    WIDTH = models.IntegerField()
    LENGTH = models.IntegerField()

    def __str__(self):
        return self.TITLE