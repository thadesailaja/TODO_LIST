from django.shortcuts import render,redirect
from todo.models import *
from todo.forms import *
from django.contrib import messages
# Create your views here.


def home(request):
    item_list=TodoList.objects.order_by('-date')
    if request.method=='POST':
        TDF=TodoForm(request.POST)
        if TDF.is_valid():
            TDF.save()
            return redirect('/home/')
    TDF=TodoForm()
    dic={'forms':TDF,'list':item_list,'title':'TODO LIST'}
    return render(request,'home.html',dic)


def remove(request,item_id):
    item=TodoList.objects.get(id=item_id)
    item.delete()
    messages.info(request,"item removed!!")
    return redirect('/home/')
