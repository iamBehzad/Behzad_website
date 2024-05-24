from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from accounts.forms import CustomUserCreationForm
from django.contrib import messages

# Create your views here.
def login_view(request):
    
    if request.user.is_authenticated:
        return redirect('/')
  
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            print('user =', user)
            if user is not None:
                login(request, user)
                return redirect('/')
        else:
            error_message = 'Invalid username or password'
            print(error_message)
            return render(request, 'accounts/login.html', {'form': form, 'error_message': error_message})
    
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')            

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        form = CustomUserCreationForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')