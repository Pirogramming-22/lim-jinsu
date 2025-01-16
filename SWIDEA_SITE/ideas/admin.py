from django.contrib import admin
from .models import Idea

class IdeaAdmin(admin.ModelAdmin):
    list_display = ('title', 'interest', 'content')  

admin.site.register(Idea, IdeaAdmin)  
