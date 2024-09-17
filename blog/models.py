from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
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
     
class BlogComment(models.Model):
     sno = models.AutoField(primary_key=True)
     comment = models.CharField(max_length=255)
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
     timeStamp = models.DateTimeField(default=now)

     def __str__(self) -> str:
          return self.comment[0:13] + "..." + "by " + self.user.username