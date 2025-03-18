from django.shortcuts import render, redirect
from .models import Task_class
from django.views.decorators.http import require_http_methods


# Create your views here.
def index(request): 
    tasks=Task_class.objects.all()
    return render(request, 'index.html', {"tasks_list": tasks})

@require_http_methods(["POST"])
def add(request):
    text=request.POST["task_text"]
    if len(text)>1:
        bool=False
        task=Task_class(task_text=text, is_it_done=bool)
        task.save()
    return redirect("index")

def done(request, task_id):
    task=Task_class.objects.get(id=task_id)
    task.is_it_done = not task.is_it_done
    task.save()
    return redirect("index")

def delete(request, task_id):
    task=Task_class.objects.get(id=task_id)
    task.delete()
    return redirect("index")

def clean (request):
    Task_class.objects.all().delete()
    return redirect("index")
