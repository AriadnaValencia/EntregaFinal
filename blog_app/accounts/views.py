from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Profile
from django.contrib.auth.views import LoginView
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('about')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html' 