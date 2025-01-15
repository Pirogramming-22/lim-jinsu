from django.shortcuts import render, get_object_or_404, redirect
from .models import Tool
from .forms import ToolForm
from django.contrib import messages

def tools_list(request):
    tools = Tool.objects.all().order_by('name') 
    return render(request, 'tools/tools_list.html', {'tools': tools})


def tools_detail(request, tool_id):
    tool = get_object_or_404(Tool, id=tool_id)
    return render(request, 'tools/tools_detail.html', {'tool': tool})

def tools_create(request):
    if request.method == "POST":
        form = ToolForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tools_list')
    else:
        form = ToolForm()
    return render(request, 'tools/tools_create.html', {'form': form})

def tools_edit(request, tool_id):
    tool = get_object_or_404(Tool, id=tool_id)  
    if request.method == 'POST':
        form = ToolForm(request.POST, instance=tool)
        if form.is_valid():
            form.save()
            return redirect('tools_detail', tool_id=tool.id)
    else:
        form = ToolForm(instance=tool) 
    return render(request, 'tools/tools_edit.html', {'form': form, 'tool': tool})

def tools_delete(request, tool_id):
    tool = get_object_or_404(Tool, id=tool_id)  
    if request.method == 'POST':  
        tool.delete()  
        messages.success(request, f"'{tool.name}' 도구가 삭제되었습니다.")
        return redirect('tools_list')  