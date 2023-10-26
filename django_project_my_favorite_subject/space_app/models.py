from django.db import models

# Create your models here.
class Mission(models.Model):
  mission_name = models.CharField(max_length=50)
  mission_type = models.CharField(max_length=50)
  mission_duration = models.CharField(max_length=20)
  mission_launch = models.CharField(max_length=20)
  
  
  
  
