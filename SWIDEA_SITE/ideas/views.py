from django.shortcuts import render, redirect, get_object_or_404
from .forms import IdeaForm
from .models import Idea 

def idea_list(request):
    sort_option = request.GET.get('sort', 'title')

    ideas = Idea.objects.all().order_by(sort_option)
    return render(request, 'ideas/ideas_list.html', {'ideas': ideas, 'sort_option': sort_option})


def idea_create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # 데이터를 저장
            return redirect('idea_list')  # 등록 후 리스트 페이지로 이동
    else:
        form = IdeaForm()

    return render(request, 'ideas/idea_create.html', {'form': form})

def idea_detail(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    return render(request, 'ideas/idea_detail.html', {'idea':idea})

def idea_update(request,pk):
    idea = get_object_or_404(Idea, pk=pk)  
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea) 
        if form.is_valid():
            form.save()  
            return redirect('idea_detail', pk=idea.pk)  # 수정 후 그 아이디어 디테일 페이지로 이동
    else:
        form = IdeaForm(instance=idea)  

    return render(request, 'ideas/idea_update.html', {'form': form, 'idea': idea})


def idea_delete(request, pk):
    idea = get_object_or_404(Idea, pk=pk)  
    idea.delete()  
    return redirect('idea_list')  

