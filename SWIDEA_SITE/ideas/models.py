from django.db import models
from tools.models import Tool
from django.contrib.auth.models import User

class Idea(models.Model):
    title = models.CharField(max_length=100) 
    image = models.ImageField(upload_to='ideas/images/', blank=True, null=True)
    content = models.TextField()  
    interest = models.IntegerField(default=0)  
    created_at = models.DateTimeField(auto_now_add=True)
    tool = models.ForeignKey('tools.Tool', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title 

class IdeaStar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idea = models.ForeignKey('Idea', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'idea')  