from django.shortcuts import redirect, render
from .models import Todo
from .forms import TodoModelForm

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    for todo in todos:
        print(todo.date_difference)    
    form = TodoModelForm()
    context = {
        'todos': todos,
        'form' : form
    }
    return render(request,'app/index.html',context)
def deleteAll(request):
    todo = Todo.objects.all()
    todo.delete()
    return redirect('/')

def add(request):
    if request.method == "POST":
        form = TodoModelForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('/')

def delete(request,pk):
    todo = Todo.objects.get(id = pk)
    todo.delete()
    return redirect('/')

def completed(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.completed = True
    todo.save()
    return redirect('/')

def not_completed(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.completed = False
    todo.save()
    return redirect('/')

def important(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.important = True
    todo.save()
    return redirect('/')


def not_important(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.important = False
    todo.save()
    return redirect('/')
