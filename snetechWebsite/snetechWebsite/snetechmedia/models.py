from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    signature = models.CharField(max_length=140, default="SNETECH MEDIA")
    