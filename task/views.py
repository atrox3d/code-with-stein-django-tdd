from django.shortcuts import render

from .models import Task
from task.forms import NewTaskForm

# Create your views here.

BORDER_WIDTH = 30
BORDER_CHAR = '/ '
BORDER = BORDER_CHAR * BORDER_WIDTH

# def bordered(fn):
#     def wrapped(*args, **kwargs):
#         print(BORDER)
#         res =  fn(*args, **kwargs)
#         print(BORDER)
#         return res
#     return wrapped

def bordered(*args, border=BORDER, **kwargs):
    print(BORDER)
    print(*args, **kwargs)
    print(BORDER)

def index(request):
    tasks = Task.objects.all()
    bordered(f'{tasks = }')

    return render(
        request, 'task/index.html', {'tasks': tasks}
    )

def detail(request, id):
    task = Task.objects.get(pk=id)
    bordered(f'{task = }')

    return render(
        request, 'task/detail.html', {'task': task}
    )

def new(request):
    form = NewTaskForm()
    return render(
        request, 
        'task/new.html',
        {'form': form}
    )
