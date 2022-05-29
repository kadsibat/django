<<<<<<< HEAD
from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from todo.models import Todo
from .forms import TodoForm
=======
from django import forms
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm

>>>>>>> 43779547f62600caefec0fad8d720af6d9000752
# Create your views here.


def home(request):
    return render(request, "todo/home.html")

<<<<<<< HEAD
def todo_list(request):
    todos = Todo.objects.all()

    context = {
        "todos": todos
        }

    return render(request, "todo/todo_list.html", context)

def todo_create(request):
    form=TodoForm(request.POST)

    if request.method == "POST" :
        form =TodoForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect("list")

    context = {
       " form ":form
    }
    
    return render(request, "todo/todo_add.html", context)

   

def todo_update(request,id):
    todo =Todo.objects.get(id=id)
    form =TodoForm(instance=todo)

    if request.method =="POST":
        form=TodoForm(request.POST,instance=todo)
=======

def todo_list(request):
    todos = Todo.objects.all()

    context = {"todos": todos}

    return render(request, "todo/todo_list.html", context)


def todo_create(request):
    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
>>>>>>> 43779547f62600caefec0fad8d720af6d9000752

        if form.is_valid():
            form.save()
            return redirect("list")
<<<<<<< HEAD
    context={
        "todo":todo,
        "form":form
    }
=======

    context = {"form": form}

    return render(request, "todo/todo_add.html", context)


def todo_update(request, id):

    todo = Todo.objects.get(id=id)
    form = TodoForm(instance=todo)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)

        if form.is_valid():
            form.save()
            return redirect("list")

    context = {"todo": todo, "form": form}
>>>>>>> 43779547f62600caefec0fad8d720af6d9000752

    return render(request, "todo/todo_update.html", context)


<<<<<<< HEAD
def todo_delete(request,id):
    todo =Todo.objects.get(id=id)
    if request.method =="POST":
        todo.delete()
        return redirect("list")

    context={
        "todo":todo
    }
    return render(request, "todo/todo_delete.html", context)

=======
def todo_delete(request, id):
    
    todo = Todo.objects.get(id=id)
    
    if request.method == "POST":
        todo.delete()
        return redirect("list")
    
    context = {
        "todo": todo
    }
    
    return render(request, "todo/todo_delete.html", context)
>>>>>>> 43779547f62600caefec0fad8d720af6d9000752
