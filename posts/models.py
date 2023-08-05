from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    #objects = models.Manager()


class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)

