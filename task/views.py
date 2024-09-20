from django.shortcuts import render

from .models import Task
# Create your views here.

BORDER_WIDTH = 30
BORDER_CHAR = '/ '
BORDER = BORDER_CHAR * BORDER_WIDTH

def index(request):
    tasks = Task.objects.all()
    print(BORDER)
    print(f'{tasks = }')
    print(BORDER)

    return render(
        request, 'task/index.html', {'tasks': tasks}
    )

def detail(request, id):
    task = Task.objects.get(pk=id)
    print(BORDER)
    print(f'{task = }')
    print(BORDER)

    return render(
        request, 'task/detail.html', {'task': task}
    )
