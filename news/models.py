from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    muallif = models.CharField(max_length=100, default='Abdurauf')

    def __str__(self):
        return self.title