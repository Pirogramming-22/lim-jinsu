from django import forms
from .models import Idea
from tools.models import Tool

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['title', 'content', 'interest', 'tool', 'image']  
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'interest': forms.NumberInput(attrs={'class': 'form-control'}),
            'tool': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
