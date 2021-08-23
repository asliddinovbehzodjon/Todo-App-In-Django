from django.shortcuts import render,redirect
from .models import Todo
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, request
from django.contrib.auth.models import User
# Create your views here.
@login_required(login_url='login')
def homepage(request):
    if request.method=='POST':
        work=request.POST['work']
        new=Todo(todo=work,user=request.user)
        new.save()
        return redirect('/')
    todos=Todo.objects.all()
    return render(request,'todo.html',{'todos':todos})
def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method=='POST':
        username=request.POST['username']
       # email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if (username is not None) and (password is not None ) and  ( password2 is not  None):
         if User.objects.filter(username = username).exists():
             form='Sorry, an account with this name has already been opened! Please choose another username!'
             return render(request,'register.html',{'form':form})
         if password==password2:
             user=User.objects.create_user(username=username,password=password)
             user.save()
             return redirect('/')


         if password2 != password:
             form="Passwords are different !!!"
             return render(request,'register.html',{'form':form})
        else:
             form="Please fill in all fields !!!"
             return render(request,'register.html',{'form':form})
    return render(request,'register.html')
###########################################
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('/')
            else:
              form="Username or password is not correct !!!"
              return render(request,'login.html',{'form':form})


        return render(request, 'login.html')
######################################
def logoutUser(request):
     logout(request)
     return redirect('/login')
    #############################
@login_required(login_url='login')
def deletetodo(request,id):
    Todo.objects.filter(id=id,user=request.user).delete()
    return redirect('/')
###### updatetodo element ###
@login_required(login_url='login')
def updatetodo(request,id):
    if request.method=='POST':
        work=request.POST['work']
        Todo.objects.filter(id=id,user=request.user).update(todo=work)
        return redirect('/')
    todo=Todo.objects.get(id=id,user=request.user)
    return render(request,'update.html',{'todo':todo})
###### finishtodo element ###
@login_required(login_url='login')
def finishtodo(request,id):
    Todo.objects.filter(id=id,user=request.user).update(status='True')
    return redirect('/')
###### continuetodo element ###
@login_required(login_url='login')
def davometish(request,id):
    Todo.objects.filter(id=id,user=request.user).update(status='False')
    return redirect('/')
