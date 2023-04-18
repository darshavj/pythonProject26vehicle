from django.shortcuts import render,redirect
from django .http import HttpResponse
from .models import *

# Create your views here.
def about(request):
    return render(request,'about.html')
def about1(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        place = request.POST['place']
        work=About(name=name,email=email,password=password,place=place)
        work.save()
        logo=Login(email=email,password=password,type=0)
        logo.save()
        return redirect("/")
def logo1(request):
    first=About.objects.all()
    dic={
        'key':first
    }
    return render(request,'home.html',dic)
def log(request):
    email = request.POST['email']
    password=request.POST['password']
    dark=Login.objects.get(email=email,password=password)
    if dark.type==0:
        request.session['email']=dark.email
        return redirect(table)
    elif dark.type==1:
        request.session['email']=dark.email
        return redirect(add)
    elif dark.type==2:
        request.session['email']=dark.email
        return redirect(super)

def add(request):
    if 'email' in request.session:
        moon = Enter.objects.all()
        status = {
            'das': moon

        }
        return render(request, 'admin.html', status)

    return redirect("/")


def super(request):
    if 'email' in request.session:
        sun = Enter.objects.all()
        data = {
            'values': sun
        }

        return render(request, 'su-admin.html', data)

    return redirect("/")

def item(request):
    return render(request,'item.html')
def item2(request):
    if request.method == 'POST':
        model = request.POST['model']
        image = request.FILES['image']
        number = request.POST['number']
        wheels = request.POST['wheels']
        description = request.POST['description']
        fun=Enter(model=model,image=image,number=number,wheels=wheels,description=description)
        fun.save()
        return redirect(item)
def table(request):
    if 'email' in request.session:
        sun = Enter.objects.all()
        data = {
            'values': sun
        }
        return render(request, 'user.html', data)

    return redirect("/")

def update(request,id):
    if request.method=='POST':
        model = request.POST['model']
        image = request.FILES['image']
        number = request.POST['number']
        wheels = request.POST['wheels']
        description = request.POST['description']
        start=Enter.objects.get(id=id)
        start.model = model
        start.image = image
        start.number = number
        start.wheels = wheels
        start.description = description
        start.save()
        return redirect(add)
    sec = Enter.objects.get(id=id)
    run = {
        'sad':sec
    }
    return render(request,'edit.html',run)
def delete(request,id):
    win=Enter.objects.get(id=id)
    win.delete()
    return redirect(super)

def logout(request):
    if 'email' in request.session:
        request.session.flush()
    return redirect(logo1)






