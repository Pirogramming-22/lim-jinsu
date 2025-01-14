from django.db import models
from tools.models import Tool

class Idea(models.Model):
    title = models.CharField(max_length=100) 
    image = models.ImageField(upload_to='ideas/images/', blank=True, null=True)
    content = models.TextField()  
    interest = models.IntegerField(default=0)  
    created_at = models.DateTimeField(auto_now_add=True)
    tool = models.ForeignKey(Tool, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title  # 관리자 화면에 제목 표시
