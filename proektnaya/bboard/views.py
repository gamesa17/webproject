from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render
from .forms import BBCreateView, AcceptReqForm, MakeReqForm
from .models import BBoard, Request, Member
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

def details(request, id):
    get_task = BBoard.objects.get(id=id)
    reqs = get_task.requests.all()
    if request.method == 'POST':
        if "sendreq" in request.POST:
            item = Request(author=request.user, author_name=request.user.username)
            form = MakeReqForm(request.POST, instance=item)
            if form.is_valid():
                get_task.requests.add(form.save())
        else:
            for item in reqs:
                buttonaccept = "принять" + str(item.id)
                buttonreject = "отклонить" + str(item.id)
                if buttonaccept in request.POST:
                    item.response = True
                    item.save()
                    req = item
                    form = AcceptReqForm(request.POST, instance=req)
                    if form.is_valid():
                        form.save()
                        upd_req = form.save()
                        new_member = Member(member=upd_req.author, member_name=upd_req.author_name)
                        new_member.save()
                        get_task.members.add(new_member)
                if buttonreject in request.POST:
                    item.response = False
                    item.save()
    form_req = MakeReqForm()
    form_accept = AcceptReqForm()
    context = {
        'title': 'Подробнее',
        'get_task': get_task,
        'form_req': form_req,
        'reqs': reqs,
        'form_accept': form_accept
    }
    print(reqs)
    return render(request, 'bboard/adprofile.html', context)

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
        bboard = BBoard(author=request.user)
        form = BBCreateView(request.POST, instance=bboard)
        if form.is_valid():
            request.user.bboards.add(form.save())
            print(request.user.bboards.all())
            return redirect('index')
    else:
        form = BBCreateView()
    return render(request, 'layout/basic2.html')

