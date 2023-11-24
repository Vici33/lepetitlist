from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Lists
from django.contrib.auth.models import User

class AddListForm(forms.ModelForm):
    class Meta:
        model = Lists
        fields = ['list_name', 'list_description', 'list_date', 'list_time', ]

    list_name = forms.CharField(widget=forms.TextInput(attrs={
        'style':'width: 100%; border-radius: 15px; padding: 20px; font-size: larger;',
    }))

    list_description = forms.CharField(widget=forms.TextInput(attrs={
        'style':'width: 100%; border-radius: 15px; padding: 20px 0px 20px 20px; font-size: larger;',
    }))

    list_date = forms.DateField(widget=forms.DateInput(attrs={
        'style':'width: 100%; border-radius: 15px; padding: 20px 0px 20px 20px; font-size: larger;',
        'type':'date',
    }))

    list_time = forms.TimeField(widget=forms.TimeInput(attrs={
        'style':'width: 100%; border-radius: 15px; padding: 20px 0px 20px 20px; font-size: larger;',
        'type':'time',
    }))


class EditForm(forms.ModelForm):
    class Meta:
        model = Lists
        fields = ['list_name', 'list_description', 'list_date', 'list_time', ]


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'style':'width: auto; border-radius: 15px; padding: 20px; font-size: larger; font-size: larger;',
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'style':'width: auto; border-radius: 15px; padding: 20px; font-size: larger; font-size: larger;',
    }))

    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'style':'width: auto; border-radius: 15px; padding: 20px; font-size: larger; font-size: larger;',
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'style':'width: auto; border-radius: 15px; padding: 20px; font-size: larger; font-size: larger;',
    }))




