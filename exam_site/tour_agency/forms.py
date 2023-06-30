from django import forms
from django.contrib.auth.models import User
from .models import Client, Application, Tour   

class LoginForm(forms.Form):
    #email = forms.CharField()
    username = forms.CharField(label='Логин',max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone_number']   
    
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Имя", "class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Фамилия", "class":"form-control"}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
    phone_number = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Номер", "class":"form-control"}), label="")

class ApplicationForm(forms.ModelForm):
    client = forms.ModelChoiceField(queryset=Client.objects.all(), widget=forms.Select(attrs={"class":"form-control"}), label="Client")
    tour = forms.ModelChoiceField(queryset=Tour.objects.all(), widget=forms.Select(attrs={"class":"form-control"}), label="Tour")
    comments = forms.CharField(required=False, widget=forms.widgets.Textarea(attrs={"placeholder":"Комментарии", "class":"form-control"}), label="")

    class Meta:
        model = Application
        fields = ['client', 'tour', 'comments']