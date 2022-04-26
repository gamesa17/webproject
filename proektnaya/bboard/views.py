from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render

from .models import BBoard

def index(requests):
    bbs = BBoard.objects.all()
    return render(requests, 'bboard/index.html', {'bbs':bbs})

def publications_spisok(requests):
    s = "Список объявлений\r\n\r\n\r\n"
    for bb in BBoard.objects.order_by('-published'):
        s += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')

penis