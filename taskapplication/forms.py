from dataclasses import fields
# from sqlite3.dbapi2 import _WindowAggregateClassp
from django import forms

from django.contrib.auth.models import User

class Registrationform(forms.ModelForm):

    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password"]

        widgets={
            "first_name":forms.TextInput(attrs={'class':'form-control'}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"}),



        }


class LoginForm(forms.Form):

    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control border border-info',"placeholder":"@Username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control border border-info',"placeholder":"enter password"}))