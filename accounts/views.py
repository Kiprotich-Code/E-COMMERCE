from django.shortcuts import render, redirect
from .forms import UserSignupForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'base.html')

def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            password = form.cleaned_data['password1']
            return redirect('login')
        else:
            raise ValueError('Invalid Form')
        
    else:
        form = UserSignupForm()
    return render(request, 'users/register.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        else: 
            raise ValueError('User doesnt exist')
        
    return render(request, 'users/login.html')
        

        
