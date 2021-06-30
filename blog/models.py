from django.db import models

class Blogpost(models.Model):
  postId = models.AutoField(primary_key=True)
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=500, default="")
  headingone = models.CharField(max_length=100)
  contentone = models.CharField(max_length=7000)
  headingtwo = models.CharField(max_length=100)
  contenttwo = models.CharField(max_length=7000)
  headingthree = models.CharField(max_length=100)
  contentthree = models.CharField(max_length=7000)
  publishDate = models.DateField()
  thumbnail = models.ImageField(default="")
  
  def __str__(self):
      return self.title
