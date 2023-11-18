from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

# Create your views here 
def home(request):
    return render(request, 'base.html')

def user_register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            return redirect('login')
        else:
            """Invalid Form"""
    
    else:
        form = RegisterUserForm()

    return render(request, 'users/register.html', {'form': form})