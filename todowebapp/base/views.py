from django.shortcuts import render,redirect
from .models import Todo
# Create your views here.

def home(request):
    todo_objs = Todo.objects.all()
    data = {'todos': todo_objs}
    return render(request,'index.html',context=data)

def create(request):
    # Data Create Request
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
    
        Todo.objects.create(name=name,description=description,status=status)
        return redirect('home')
    return render(request,'create.html')

def edit(request,pk):
    todo = Todo.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        todo.name = name
        todo.description = description
        todo.status = status
        todo.save()
        return redirect('home')
    data = {'todo': todo}
    return render(request,'edit.html',context=data)

def delete(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('home')
