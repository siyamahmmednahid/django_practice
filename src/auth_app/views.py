from django.shortcuts import render
from auth_app import forms

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    homeDict = {'title': 'Home Page'}
    return render(request, 'auth_app/index.html', context=homeDict)


# For registration
def register(request):
    registered = False
    if request.method == 'POST':
        userForm = forms.UserForm(data=request.POST)
        userInfoForm = forms.UserInfoForm(data=request.POST)

        if userForm.is_valid() and userInfoForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()

            userInfo = userInfoForm.save(commit=False)
            userInfo.user = user
            if 'profile_pic' in request.FILES:
                userInfo.profile_pic = request.FILES['profile_pic']
            userInfo.save()
            registered = True
    else:
        userForm = forms.UserForm()
        userInfoForm = forms.UserInfoForm()
    registerDict = {'title': 'Register Page', 'userForm': userForm, 'userInfoForm': userInfoForm, 'registered': registered}
    return render(request, 'auth_app/register.html', context=registerDict)


# For login
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('auth_app:index'))
            else:
                return HttpResponse('Account not active')
        else:
            return HttpResponse('Invalid login details supplied')
    else:
        return render(request, 'auth_app/login.html')


# For logout
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('auth_app:index'))