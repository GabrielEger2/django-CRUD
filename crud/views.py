from django.shortcuts import render, redirect
from .models import User 

def home(request):
    users = User.objects.all()
    return render(request, "index.html", {"users": users})

def save(request):
    name = request.POST.get("name")
    User.objects.create(name=name)
    users = User.objects.all()
    return render(request, "index.html", {"users": users})

def edit(request, id):
    user = User.objects.get(id=id)
    return render(request, "update.html", {"user": user})

def update(request, id):
    newName = request.POST.get("name")
    user = User.objects.get(id=id)
    user.name = newName
    user.save()
    return redirect(home)

def delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect(home)
