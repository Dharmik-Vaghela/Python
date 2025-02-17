from django.shortcuts import render
from .models import *

# Create your views here.
def Registerpage(request):
    return render(request,"app/register.html")

def UserRegister(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        
        user = User.objects.filter(Email=email)
        if user:
            message = "User Already Exists"
            return render(request,"app/login.html",{'msg':message})
        else:
             if password == cpassword:
                 newuser = User.objects.create(Firstname=fname, Lastname=lname, Email=email, Contact=contact, Password=password)
                 message = "User Registered Successfully"
                 return render(request,"app/login.html",{'msg':message})
             else:
                 message = "Password and Confirm Password does not match"
                 return render(request,"app/register.html",{'msg':message})
             
def Loginpage(request):
    return render(request,"app/login.html")

def LoginUser(request):
    if  request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']
        
        user = User.objects.get(Email=email)
        if user.Password == password:
            request.session['Firstname'] = user.Firstname
            request.session['Lastname'] = user.Lastname
            request.session['Email'] = user.Email
            return render(request,"app/home.html")
        else:
            message = "Incorrect Password"
            return render(request,"app/login.html",{'msg':message})
    else:
        message = "User does not exist"
        return render(request,"app/register.html",{'msg':message})
        