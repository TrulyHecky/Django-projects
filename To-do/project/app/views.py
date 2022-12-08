from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


def index(request):
    form = Todo.objects.all()
    context = {
        "form": form
    }
    return render(request, "app/index.html", context)


def add(request):
    form = TodoForm
    if request.method == "POST":
        form = TodoForm(request.POST)
        form.save()
        return redirect("index")

    context = {
        "form": form
    }
    return render(request, "app/add.html", context)


def delete(request, id):
    form = Todo.objects.get(id=id)
    form.delete()
    return redirect("index")


def edit(request, id):
    todo_id = Todo.objects.get(id=id)
    form = TodoForm(instance=todo_id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo_id)
        if form.is_valid():
            form.save()
            return redirect("index")

    context = {
        "form": form
    }
    return render(request, "app/edit.html", context)
