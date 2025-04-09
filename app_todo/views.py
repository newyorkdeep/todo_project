from django.shortcuts import render, redirect
from .models import Task_class
from .models import Themepicker
from django.views.decorators.http import require_http_methods
from django.template import loader
from django.http import HttpResponse


# Create your views here.
def index(request): 
    userpreference=Themepicker.objects.all()
    if len(userpreference)==0:
        a=Themepicker(is_it_black="False", tag="tag")
        a.save()
    tasks=Task_class.objects.all()
    query = Themepicker.objects.filter(tag="tag")[0]
    variable = query.is_it_black
    return render(request, 'index.html', {"tasks_list": tasks, 'variable': variable})

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

def about (request):
    query = Themepicker.objects.filter(tag="tag")[0]
    variable = query.is_it_black
    return render(request, 'about.html', {'variable': variable})

def switch(request): 
    query = Themepicker.objects.filter(tag="tag")[0]
    query.is_it_black=not query.is_it_black
    query.save()
    return redirect("index")