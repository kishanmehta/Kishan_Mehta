from django.shortcuts import render, redirect
from .models import Contact
from django.db import Error
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def index(request):
    contact = Contact.objects.all()
    return render(request,"index.html",{'contact':contact})

def add(request):
    return render(request,'add.html')

def addrec(request):
    try:
        x=request.POST.get("name")
        y=request.POST.get("email")
        z=request.POST.get("notes")
        cont = Contact(name=x,email=y,notes=z)
        validate_email(y)
        cont.save()
        return redirect("/")
    except (ValidationError, Error) as e:
        return render(request,'add.html',{'error_message': e})


def delete(request,name):
    cont = Contact.objects.get(name=name)
    return render(request,'delete.html',{'cont':cont})

def deleterec(request,name):
    cont = Contact.objects.get(name=name)
    cont.delete()
    return redirect("/")

def update(request,name):
    cont = Contact.objects.get(name=name)
    return render(request,'update.html',{'cont':cont})

def uprec(request,name):
    x=request.POST.get("name")
    y=request.POST.get("email")
    z=request.POST.get("notes")
    cont = Contact.objects.get(name=name)
    cont.name = x
    cont.email = y
    cont.notes = z
    cont.save()
    return redirect("/")

def details(request,name):
    cont = Contact.objects.get(name=name)
    return render(request,'details.html',{'cont':cont})