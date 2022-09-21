from django.contrib.auth.models import User
from django import forms
from auth_app.models import UserInfo


# Create your models here.
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta():
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class UserInfoForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ('portfolio_site', 'profile_pic')
        widgets = {
            'portfolio_site': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
        }