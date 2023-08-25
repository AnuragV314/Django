from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def homePage(request):
    user = User.objects.all()
    return render(request, 'home.html', {'user':user})



def loginPage(request):
    # user = User.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        userpassword = request.POST.get('password')
        print(username, userpassword)
        user = authenticate(request, username=username, userpassword=userpassword)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/home/')
        else:
            return HttpResponse('invalid name or password')
    return render(request, 'login.html', {})



def signupPage(request):
    if request.method == "POST":

        # data fetch
        username = request.POST.get('username')
        useremail = request.POST.get('useremail')
        userpassword = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        userphone = request.POST.get('userphone')
        useraddress = request.POST.get('useraddress')

        # validate

        if userpassword != confirmpassword:
            return HttpResponse("password and confirm password does't match")
        
        # create model object and set the data
        u = User()
        u.username = username
        u.useremail = useremail
        u.userpassword = userpassword
        u.confirmpassword = confirmpassword
        u.userphone = userphone
        u.useraddress = useraddress

        # save data
        u.save()
 
        # prepare message
        # print(username, useremail,userpassword, userphone, useraddress)
        return redirect('/login/')

    return render(request, 'signup.html', {})