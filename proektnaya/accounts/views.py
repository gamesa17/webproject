from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect


# class SignUpView(generic.CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'accounts/signup.html'

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})


def showprofile(request):
    profile = CustomUser.objects.all()
    return render(request, 'accounts/my_profile.html', {'title': 'Главная страница', 'profile': profile})
