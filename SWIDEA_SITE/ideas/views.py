from django.shortcuts import render, redirect, get_object_or_404
from .forms import IdeaForm
from .models import Idea, IdeaStar
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def idea_list(request):
    sort_option = request.GET.get('sort', 'title')
    ideas = Idea.objects.all().order_by(sort_option)

    # 찜 여부 추가
    for idea in ideas:
        idea.is_starred = IdeaStar.objects.filter(user=request.user, idea=idea).exists()

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
    user = request.user
    is_starred = IdeaStar.objects.filter(user=user, idea=idea).exists() if user.is_authenticated else False
    return render(request, 'ideas/idea_detail.html', {'idea': idea, 'is_starred': is_starred})

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

def toggle_star(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    user = request.user
    existing_star = IdeaStar.objects.filter(user=user, idea=idea).first()
    if existing_star:
        existing_star.delete()
    else:
        IdeaStar.objects.create(user=user, idea=idea)

    return redirect('idea_list')
        
@csrf_exempt
def adjust_interest(request, idea_id):
    if request.method == 'POST':
        action = request.POST.get('action', None)  # 수정된 부분
        try:
            idea = Idea.objects.get(id=idea_id)
            if action == 'increase':
                idea.interest += 1
            elif action == 'decrease' and idea.interest > 0:
                idea.interest -= 1
            idea.save()
            return JsonResponse({'success': True, 'new_interest': idea.interest})
        except Idea.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Idea not found'}, status=404)
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=400)