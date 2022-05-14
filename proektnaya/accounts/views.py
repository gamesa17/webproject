from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import CustomUser
from .forms import CustomUser
from django.shortcuts import render, redirect


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


def showprofile(request):
    #profile = request.user
    profile = CustomUser.objects.all()
    context = {'profile': profile}
    #print(request.user.is_authenticated())
    return render(request, 'bboard/users.html', context)


