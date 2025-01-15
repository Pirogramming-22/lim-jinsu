from django.contrib import admin
from .models import Idea

class IdeaAdmin(admin.ModelAdmin):
    list_display = ('title', 'interest', 'content')  # 관리자 화면에 표시할 필드

admin.site.register(Idea, IdeaAdmin)  # 모델과 관리자 설정을 등록
