from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import CustomUser
from .forms import CustomUser
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm


# class SignUpView(generic.CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'accounts/signup.html'

def register(request):
    if request.method == 'POST':
        print(request.POST)

        form = CustomUserCreationForm(request.POST)


        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = CustomUserCreationForm()

    print('form is not valid', form.errors)
    return render(request, 'bboard/profile.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
            else:
                return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def showprofile(request):
    #profile = request.user
    profile = CustomUser.objects.all()
    context = {'profile': profile}
    #print(request.user.is_authenticated())
    return render(request, 'bboard/users.html', context)


