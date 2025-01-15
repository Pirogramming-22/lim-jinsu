from django.urls import path
from . import views

urlpatterns = [
    path('', views.idea_list, name='idea_list'),  # 메인 페이지
    path('new/', views.idea_create, name='idea_create'),  # 등록 페이지
    path('<int:pk>/', views.idea_detail, name='idea_detail'),
    path('<int:pk>/edit/', views.idea_update, name='idea_update'),  
    path('<int:pk>/delete/', views.idea_delete, name='idea_delete'),  
]
