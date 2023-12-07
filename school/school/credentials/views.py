from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from storeapp.views import home


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('new_page')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request,"login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email Taken")
                return redirect('register')
            else:
                 user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                            last_name=last_name, email=email)
                 user.save();
                 return redirect('login')
        else:
           messages.info(request,"password not match")
           return redirect('register')
           return  redirect('/')

    return render(request,"register.html")

def department(request):
    department=request.POST['department']
    wikipedia_link=request.POST['wikipedia_link']
    user=authenticate(department=department,wikipedia_link=wikipedia_link)
    if user is not None:
        department(request,user)
        return redirect('/')
    else:
        pass
    return render(request,'department.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

def new_page(request):
    new_page(request,'newpage.html')
    return redirect('form')

def form(request):
    if request.method == 'POST':
        name=request.POST['name']
        dob = request.POST['dob']
        gender = request.POST['gender']
        phoneno = request.POST['phoneno']
        email = request.POST['email']
        address = request.POST['address']
        department = request.POST['department']
        courses = request.POST['courses']
        purpose = request.POST['purpose']
        material = request.POST['material']
        user=authenticate(name=name,dob=dob,gender=gender,phoneno=phoneno,
                          email=email,address=address,department=department,
                          courses=courses,purpose=purpose,material=material)
        if user is not None:
            form(request,user)
            return redirect('/')
        else:
            pass
    return render(request,'form.html')
