from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Your Account Has Been Created !!. Please login with the new account now')
            return redirect('login')

            # Optionally, you can redirect to a success page or login the user
            
    form= UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

