from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
        
class Blog(models.Model):    
    title = models.CharField(max_length=80,null=True)
    author=models.CharField(max_length=60)
    date_posted = models.DateTimeField(auto_now_add=True,null=True)
    description= models.CharField(max_length=400,null=True,blank=True)   
    image=models.ImageField(upload_to='gallery')
  

    def __str__(self):
        return self.title

   

        
