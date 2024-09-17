from django.db import models

# Create your models here.
class Post(models.Model):
     sno= models.AutoField(primary_key=True)
     title = models.CharField(max_length=255)
     author = models.CharField(max_length=100)
     content= models.TextField()
     timeStamp=models.DateTimeField(blank=True)
     slug = models.CharField(max_length=130)

     def __str__(self) -> str:
          return self.title + ' - ' + self.author