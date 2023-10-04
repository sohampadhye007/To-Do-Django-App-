from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks=Task.objects.filter(is_completed=False).order_by('updated_at') 
    # get will fetch only one data, we want filtered data
    # print(tasks)
    # <QuerySet [<Task: complete assignment>, <Task: learn django>]>
    context = {
        'tasks': tasks,
    }
    return render(request, 'home.html', context)