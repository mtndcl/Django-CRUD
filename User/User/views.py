from django.shortcuts import render

from .forms import RegisterForm
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib import messages



def login_page(request):
    

    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(request,username=username, password=password)

        print('login page work here ---------------------------------',username,password)
        if user is not None:
            login(request, user)

            return HttpResponseRedirect(reverse('profile-page'))
        else:

            messages.warning(request, 'Your username or password wrong')
            print('failed log in---------------------------',username,password)
            return HttpResponseRedirect(reverse('login-page'))
    else:
        return render(request, 'User/login.html', {})
    
    
def profile(request):


    return render(request, 'User/profile.html')