from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Link task to logged-in user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'accounts/task_list.html', {
        'tasks': tasks,
        'form': form
    })
