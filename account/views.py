from django.shortcuts import render,redirect
from account.models import User
from django.contrib import messages

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

        print("//////////////////////////////////////////////////////")
        print(fname,lname,mobile,email,pass1,pass2)

    

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
    return render(request ,'login.html')

# Create your views here.
