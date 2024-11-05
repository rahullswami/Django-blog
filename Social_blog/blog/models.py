from django.db import models

# Create your models here.
class Blog_post(models.Model):
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    post = models.ImageField(upload_to='post')
    disc = models.TextField(max_length=1000)

    def __str__(self):
        return self.username
    