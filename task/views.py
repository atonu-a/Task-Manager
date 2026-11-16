from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

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
        data = request.POST
        taskCreationForm = TaskCreationForm(data)
        if taskCreationForm.is_valid():
            task =  taskCreationForm.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("home")
            
        else:
            taskCreationForm = TaskCreationForm()         
    
    context= {
        'taskCreationForm' : taskCreationForm,
    }
    return render(request, 'base.html', context)

@login_required
def task_details(request, title):
    task = get_object_or_404(Task, title = title, user = request.user)
    return render(request, '', {'task':task})



@login_required
def delete_task(request, title):
    task = get_object_or_404(Task, title = title, user = request.user)
    task.delete()
    return redirect("home")


@login_required
def mark_as_completed(request, title):
    task = get_object_or_404(Task, title = title, user = request.user)
    task.is_completed = True
    task.save()
    return redirect("home")


@login_required
def edit_task(request, title):
    task = get_object_or_404(Task, title = title, user = request.user )
    if request.method == 'POST':
        data = request.POST
        taskCreationForm = TaskCreationForm(data, instance=task)
        if taskCreationForm.is_valid():
            taskCreationForm.save(commit=False)
            return redirect("home")
            
        else:
            taskCreationForm = TaskCreationForm(instance=task)         
    
    context= {
        'taskCreationForm' : taskCreationForm,
    }
    return render(request, 'base.html', context)

def register(request):
    if request.method == "POST":    
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('home')
        else:
            form = UserCreationForm()
            
        return render(request, "register.html", {'form' : form })
    

    