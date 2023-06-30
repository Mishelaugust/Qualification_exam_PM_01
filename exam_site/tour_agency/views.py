from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Application
from .forms import LoginForm, ClientForm, ApplicationForm




def home(request):
    app_list = Application.objects.all()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request,'Вход успешен!')
                return redirect('home')
            else:
                messages.success(request,'Неверные данные!')
                return redirect('home')
        # else:
        #     messages.success(request,'Неккоректные данные!')
        #     return redirect('home')

    else:
        form = LoginForm()
    return render(request, 'home.html', {'form': form, 'app_list': app_list})



def logout_user(request):
    logout(request)
    messages.success(request, "Вы вышли из системы!")
    return redirect('home')

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace 'client_list' with the URL name of the client list view
    else:
        form = ClientForm()
    
    return render(request, 'add_client.html', {'form': form})

def add_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace 'application_list' with the URL name of the application list view
    else:
        form = ApplicationForm()
    
    return render(request, 'add_application.html', {'form': form})


def update_application(request, pk):
    application = Application.objects.get(id=pk)

    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace 'application_list' with the URL name of the application list view
    else:
        form = ApplicationForm(instance=application)
    
    return render(request, 'update_application.html', {'form': form})


def delete_application(request, pk):
    manager_record = Application.objects.get(id=pk)
    manager_record.delete()
    messages.success(request, f"Заявка удалена!")
    return redirect('home')
