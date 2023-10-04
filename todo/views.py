from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from . models import Task

def addTask(request):
    task= request.POST['task'] # POST not post 
    # name of the class is task therefore we have written 'task'
    # <input type="text" name="task" class="form-control" placeholder="Add a task">
    Task.objects.create(task=task) # task is coming from models.py ----> Task ----> task
    return redirect('home')

# Create your views here.
