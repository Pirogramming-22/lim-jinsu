from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Post, Comment

def post_list(request):
    posts = Post.objects.all()  # 데이터베이스에서 모든 게시물 가져오기
    return render(request, 'posts/post_list.html', {'posts': posts})


def toggle_like(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        if post.like_count > 0: #이미 좋아요 누른 상태면
            post.like_count -= 1
        else: #좋아요 누르지 않았으면
            post.like_count += 1
        post.save()
        return JsonResponse({"like_count":post.like_count})
    return JsonResponse({"error": "Invalid request"}, status=400)

def add_comment(request, post_id):
    if request.method == "POST":
        content = request.POST.get("content")  # 요청에서 댓글 내용 가져오기
        if not content:
            return JsonResponse({"error": "댓글 내용을 입력해주세요."}, status=400)

        post = get_object_or_404(Post, id=post_id)  # 해당 게시물 가져오기
        comment = Comment.objects.create(post=post, content=content)  # 댓글 생성
        return JsonResponse({
            "id": comment.id,
            "content": comment.content,
            "created_at": comment.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        })
    return JsonResponse({"error": "Invalid request"}, status=400)

def delete_comment(request, comment_id):
    if request.method == "POST":
        comment = get_object_or_404(Comment, id=comment_id)  
        comment.delete() 
        return JsonResponse({"message": "댓글이 삭제되었습니다.", "id": comment_id})
    return JsonResponse({"error": "Invalid request"}, status=400)