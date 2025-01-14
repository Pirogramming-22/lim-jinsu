from django.urls import path
from . import views

urlpatterns = [
    path('', views.tools_list, name='tools_list'),  # 리스트 페이지
    path('new/', views.tools_create, name='tools_create'),
    path('<int:tool_id>/', views.tools_detail, name='tools_detail'),  # 디테일 페이지
    path('<int:tool_id>/edit/', views.tools_edit, name='tools_edit'), # 수정
    path('<int:tool_id>/delete/', views.tools_delete, name='tools_delete'), #삭제
]
