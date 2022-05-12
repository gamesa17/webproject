from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import BBoard
from .models import Rubric
from .forms import BBForm

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

class BBCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BBForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

def CompanyView(request, id):
    all_objects = BBoard.objects.get(id=id)
    context = {'all_objects':all_objects}
    return render(request, 'bboard/company_view.html', context)

def auth(request):
    return render(request, 'bboard/auth.html')

def adprofile(request):
    return render(request, 'bboard/adprofile.html')

def reg_user(request):
    return render(request, 'bboard/adprofile.html')

def login_user(request):
    return render(request, 'accounts/login.html')


