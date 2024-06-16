from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def HomePage(request):
    return render(request,'app/home.html')

def InsertPageView(request):
    return render(request,"app/insert.html")

def InsertData(request):
    #Data come from HTML to view
    fname = request.POST['firstname']   
    lname = request.POST['lastname']
    email = request.POST['email']
    contact = request.POST['contact']
    
    #creating object of model class
    newuser = Student.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact)
    
    #After insert render on show.html
    return redirect('showpage')

def ShowPage(request):
    all_data = Student.objects.all()
    return render(request,"app/show.html",{'key1':all_data})

def EditPage(request,pk):
    get_data=Student.objects.get(id=pk)
    return render(request,"app/edit.html",{'key2':get_data})

def UpdateData(request,pk):
    udata = Student.objects.get(id=pk)
    udata.Firstname = request.POST['firstname']
    udata.Lastname = request.POST['lastname']
    udata.Email = request.POST['email']
    udata.Contact = request.POST['contact']
    udata.save()
    return redirect('showpage')

def DeleteData(request,pk):
    ddata = Student.objects.get(id=pk)
    ddata.delete()
    return redirect('showpage')