from django.shortcuts import render,redirect
from django.http import HttpResponse
from account.models import User
from django.contrib import messages
from django.contrib.auth import authenticate ,login,logout

# Create your views here.

def handleSignup(request):
    if request.method == 'POST':
        #Get teh post parameters
        
        fname=request.POST['fname']
        lname=request.POST['lname']
        mobile=request.POST['mobile']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # print("//////////////////////////////////////////////////////")
        # print(fname,lname,mobile,email,pass1,pass2)

    

        if pass1 != pass2:
            messages.error(request, 'password dose not match')
            return redirect('handlesignup')
        
        myuser = User.objects.create_user(email,pass1)
        
        myuser.first_name =fname
        myuser.last_name =lname
        myuser.mobile = mobile
        myuser.save()
      
        messages.success(request, "Profile details updated.")
        
        return redirect('handleSignup')

    return render(request ,'signup.html')

def index(request):
    return render(request ,'home.html')


def handlelogin(request):

    if request.method == 'POST':
        loginemail = request.POST['loginemail']
        loginpass = request.POST['loginpass']

        user = authenticate(email=loginemail, password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('index')
        else:
            messages.error(request, "Invalid Details")
            return redirect('index')

    return render(request ,'login.html')
    # return HttpResponse("404 Error")

# Create your views here.


def showusers(request):
    user = User.objects.all()

    print("ssssssssssssssssssssssssssssssssssssssssssssssssssssssss") 
    for u in user:
        print(u.username)
        print(u.first_name )
    
    return render(request, 'showuser.html', {'user':user})


def handlelogout(request):
    logout(request)
    messages.success(request, 'Logout successfully')
    return redirect('index')