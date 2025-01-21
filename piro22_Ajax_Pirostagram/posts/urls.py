from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # 첫 화면
    path('like/<int:post_id>/', views.toggle_like, name='toggle_like'),  # 좋아요 URL
    path('comment/add/<int:post_id>/', views.add_comment, name='add_comment'),  # 댓글 추가 URL
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),  # 댓글 삭제 URL
]
