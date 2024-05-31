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
        return redirect('/')  # Redirect to the index page
  
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            print('user =', user)
            if user is not None:
                login(request, user)
                return redirect('/')  # Redirect to the index page
            else:
                error_message = 'Invalid username or password'
                messages.add_message(request, messages.ERROR, error_message)
                return render(request, 'accounts/login.html', {'form': form})
        else:
            error_message = 'Invalid username or password'
            messages.add_message(request, messages.ERROR, error_message)
            return render(request, 'accounts/login.html', {'form': form})
    
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
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