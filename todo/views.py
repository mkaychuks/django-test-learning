from django.shortcuts import render, get_object_or_404, redirect


from .models import Todo
from .forms import TodoForm


def list_todo(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    template_name = 'index.html'
    return render(request, template_name, context)


def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    context = {
        'todo': todo
    }
    template_name = 'detail.html'
    return render(request, template_name, context)


def create_todo(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    context = {
        'form': form
    }
    template_name = 'form.html'
    return render(request, template_name, context)

def update_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    context = {
        'form': form
    }
    template_name = 'update.html'
    return render(request, template_name, context)