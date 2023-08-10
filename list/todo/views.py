from django.shortcuts import render,HttpResponseRedirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    if request.method=='POST':
        fm = TodoForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = TodoForm()
    to = Todo.objects.all()
    return render(request,'index.html',{'to':to,'fm':fm})

def delete_data(request,id):
    if request.method=='POST':
        pi = Todo.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')

def update_data(request,id):
    if request.method=='POST':
        pi = Todo.objects.get(pk=id)
        fm = TodoForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Todo.objects.get(pk=id)
        fm = TodoForm(instance=pi)
    return render(request,'update.html',{'fm':fm})    