from django.db import models

# Create your models here.


class UploadCloud(models.Model):
    title= models.CharField(max_length=300)
    text=models.TextField()

    def __str__(self):
        return self.title
