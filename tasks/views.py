from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Task
from django.contrib.auth.decorators import login_required
from . forms import *



@login_required
def home(request):
    lis = Task.objects.filter(deleted=False, user = request.user)
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.user = request.user
            new.save()
            return redirect('/')

    context = {'lis':lis, 'form':form}
    return render(request, 'tasks/index.html', context)


def updateTask(request, pk):
    single = Task.objects.get(id=pk)

    form = TaskForm(instance=single)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=single)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'single':single, 'form':form}
    return render(request, 'tasks/single.html', context)


def taskDelete(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        dele = form.save(commit=False)
        dele.deleted = True
        dele.save()
        return redirect('home')

    context = {'task':task, 'form':form}
    return render(request, 'tasks/confirm.html', context)


def taskComp(request, pk):
    comp = Task.objects.get(id=pk)
    comp.completed = True
    comp.save()
    return redirect('home')
