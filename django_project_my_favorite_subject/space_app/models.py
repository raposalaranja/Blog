from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mission(models.Model):
  mission_name = models.CharField(max_length=50)
  mission_type = models.CharField(max_length=50)
  mission_duration = models.CharField(max_length=20)
  mission_launch = models.CharField(max_length=20)
  
  def __str__(self):
    return f"{self.mission_name}"
  
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)  
    
def __str__(self):
  return f"{self.title}"
  
  
  
  
