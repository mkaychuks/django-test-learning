from django.shortcuts import render,get_object_or_404


from .models import Todo


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
