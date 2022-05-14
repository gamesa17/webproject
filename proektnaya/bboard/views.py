from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render
from .forms import BBCreateView
from .models import BBoard
from .models import Rubric
from .forms import BBForm
from django.shortcuts import render, redirect

def index(request):
    bbs = BBoard.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs':bbs, 'rubrics':rubrics}
    return render(request, 'layout/basic2.html', context)

def publications_spisok(request):
    s = "Список объявлений\r\n\r\n\r\n"
    for bb in BBoard.objects.order_by('-published'):
        s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')

def by_rubric(request, rubric_id):
    bbs = BBoard.objects.filter(rubric = rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk = rubric_id)
    context = {'bbs':bbs, 'rubrics':rubrics, 'current_rubric':current_rubric}
    return render(request, 'bboard/by_rubric.html', context)


def CompanyView(request, id):
    all_objects = BBoard.objects.get(id=id)
    context = {'all_objects':all_objects}
    return render(request, 'bboard/company_view.html', context)

def auth(request):
    return render(request, 'bboard/auth2.html')

def login_user(request):
    result = request.GET.get('login')
    return JsonResponse(data)

def profile(request):
    user = request.user
    context = {'user':user}
    return render(request, 'bboard/profile.html', context)

def adcreate(request):
    return render(request, 'bboard/adcreate.html')

def createnew(request):
    if request.method == 'POST':
        form = BBCreateView(request.POST)


        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = BBCreateView()

    return render(request, 'layout/basic2.html')

