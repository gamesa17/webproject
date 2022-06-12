from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout


# class SignUpView(generic.CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'accounts/signup.html'

def register(request):
    if request.method == 'POST':

        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            print(request.user)
            return redirect('profile')

    else:
        form = CustomUserCreationForm()

    print('form is not valid', form_reg.errors)
    return render(request, 'bboard/profile.html')


def user_login(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    print("Получилось")
                    login(request, user)
                    return redirect('profile')
            else:
                return redirect('auth')
    else:
        form = LoginForm()
    return render(request, 'bboard/profile.html')

def editname(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.user.username)
        for p in request.POST:
            print(p)
        request.user.username = request.POST['user_name']
        print(request.user.username)
        request.user.save()
        redirect('profile')
    return render(request, 'bboard/profile.html')

def editemail(request):
    if request.method == 'POST':
        print(request.POST)
        request.user.email = request.POST['email']
        print(request.user.email)
        request.user.save()
        redirect('profile')

    return render(request, 'bboard/profile.html')

def showprofile(request):
    #profile = request.user
    profile = CustomUser.objects.all()
    context = {'profile': profile}
    #print(request.user.is_authenticated())
    return render(request, 'bboard/users.html', context)


