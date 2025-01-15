from django.contrib import admin
from django.urls import path, include
from ideas import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.idea_list, name='idea_list'),  # 첫 화면
    path('ideas/', include('ideas.urls')),  # 아이디어 앱
    path('tools/', include('tools.urls')), # 툴스 앱
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)