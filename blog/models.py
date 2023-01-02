from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    blog_title = models.CharField(max_length=200)
    blog_content = models.TextField()
    updated_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.blog_title
    
 
 
   
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    blog =  models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment_content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return str(self.id)
    
