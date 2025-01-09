from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 홈 화면
    path('review/<int:review_id>/', views.detail, name='detail'),  # 디테일 페이지
    path('review/create/', views.create, name='create'),  # 리뷰 작성 페이지
    path('review/<int:review_id>/update/', views.update, name='update'),  # 수정 페이지
    path('review/<int:review_id>/delete/', views.delete, name='delete'),  # 삭제 페이지
]
