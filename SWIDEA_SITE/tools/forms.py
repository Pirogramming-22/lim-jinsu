from django import forms
from .models import Tool

class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ['name', 'description', 'category']  
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '도구 이름'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '카테고리 입력'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '도구 설명'}),
        }
