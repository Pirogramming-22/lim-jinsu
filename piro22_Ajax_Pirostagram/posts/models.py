from django.db import models

class Post(models.Model):
    title = models.CharField('게시물 제목', max_length=100) 
    image = models.ImageField('이미지', upload_to='images/%Y%m%d', blank=True)
    content = models.TextField('게시물 내용')  
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="등록일") 
    like_count = models.IntegerField(default=0, verbose_name="좋아요 수")  

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")  
    content = models.TextField('댓글 내용')  
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일")  

    def __str__(self):
        return self.content
