from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def InsertPage(request):
    return render(request,'app/insert.html')

def InsertData(request):
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        salary = request.POST['salary']
        email = request.POST['email']
        contact = request.POST['contact']
        newuser = Teacher.objects.create(
                Firstname=fname,
                Lastname=lname,
                Salary=salary,
                Email=email,
                Contact=contact
            )
        return redirect('showdata')


def ShowData(request):
    all_data = Teacher.objects.all()
    return render(request,'app/show.html',{'key_1':all_data})

def EditPage(request,pk):
    get_data = Teacher.objects.get(id=pk)
    return render(request,'app/edit.html',{'key_2':get_data})
    
def UpdateData(request, pk):
    getid = Teacher.objects.get(id=pk)
    getid.Firstname = request.POST['firstname']
    getid.Lastname = request.POST['lastname']
    getid.Salary = request.POST['salary']
    getid.Email = request.POST['email']
    getid.Contact = request.POST['contact']
    getid.save()
    return redirect('showdata')


def DeleteData(request,pk):
    del_data = Teacher.objects.get(id=pk)
    del_data.delete()
    return redirect('showdata')