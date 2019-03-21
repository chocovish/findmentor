from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self): return self.name


class User(AbstractUser):
    usertype = models.CharField(max_length=1,choices=(('M','Mentor'),('S','Start Up')),blank=True,null=True)
    user_cat = models.ManyToManyField(Category,blank=True,null=True)
    headline = models.CharField(max_length=200,null=True,blank=True)
    l_id = models.CharField(max_length=10)
    dp = models.URLField(null=True,blank=True)
    


