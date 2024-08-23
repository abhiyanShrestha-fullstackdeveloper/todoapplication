from django.shortcuts import render
from .models import Todo
# Create your views here.

def home(request):
    todo_objs = Todo.objects.all()
    data = {'todos': todo_objs}
    return render(request,'index.html',context=data)
