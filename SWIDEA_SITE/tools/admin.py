from django.contrib import admin
from .models import Tool

class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')  # 관리자 화면에 표시할 필드
    search_fields = ('name', 'category')  # 검색 필드

admin.site.register(Tool, ToolAdmin)