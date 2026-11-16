from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TaskCreationForm
from .models import Task

# Create your views here.

@login_required
def home(request):
    status = request.GET.get('status', 'all')
    category = request.GET.get('category', 'all')
    tasks = Task.objects.filter(user = request.user)
    
    
    if status != "all":
        tasks = tasks.filter(is_compleled=(status=='Completed'))
    if category != "all":
        tasks = tasks.filter(category=category)
        
    completed_tasks = tasks.filter(is_completed = True)
    pending_tasks = tasks.filter(is_completed = False)
    context = {
        "completed_tasks" : completed_tasks,
        'pending_tasks' : pending_tasks,
        'status' : status,
        'category' : category,
        'tasks' : tasks,
        
    }
    
    return render(request,'base.html', context)

@login_required
def create_task(request):
    if request.method == 'POST':
        taskCreationForm = TaskCreationForm(request.POST)
        if taskCreationForm.is_valid():
            taskCreationForm.save()
            
        else:
            taskCreationForm = TaskCreationForm()         
    
    context= {
        'taskCreationForm' : taskCreationForm,
    }
    return render(request, 'base.html', context)

