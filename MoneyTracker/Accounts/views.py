from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('Home')

def registeration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('Home')  # Redirect to the desired URL after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})
