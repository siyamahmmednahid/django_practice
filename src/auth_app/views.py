from django.shortcuts import render
from auth_app import forms

# Create your views here.
def index(request):
    homeDict = {'title': 'Home Page'}
    return render(request, 'auth_app/index.html', context=homeDict)


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
