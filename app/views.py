from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models import *


# Create your views here.


def display_topicname(request):
    QLTO = Topic.objects.all()
    #QLTO=Topic.objects.filter(topic_name='cricket')
    #QLTO=Topic.objects.filter(topic_name='football')
    
    d={'topics':QLTO}
    return render(request,'display_topicname.html',d)

def webpage(request):
    QLWO= Webpage.objects.all()
    QLWO= Webpage.objects.all()
    QLWO= Webpage.objects.filter(name__startswith='v')
    QLWO= Webpage.objects.filter(url__endswith='com')
    QLWO= Webpage.objects.filter(name__contains ='r')
    QLWO= Webpage.objects.filter(name__regex ='\w+$')
    QLWO= Webpage.objects.filter(Q(name='virat') | Q(url__startswith='https'))    
    QLWO= Webpage.objects.filter(Q(name='Rahul') & Q(url__startswith='https'))     
    d={'webpage':QLWO}
    return render(request,'Webpage.html',d)


def AccessRecord(request):
    QARO =AccessRecord.objects.all()
    QARO=AccessRecord.objects.filter(dtae__gt='2022-10-10')


    d={'access':QARO}
    return render(request,'AccessRecord.html',d)

def insert_topics(request):
    tn=input('Enter the topic_name: ')
    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()
    return render('Topic is created')

def insert_web(request):
    tn=input('Enter value: ')
    n=input('Enter name: ')
    u=input('Enter url: ')
    e=input('Enter email: ')
    To=Topic.objects.get_or_create(topic_name=tn)[0]
    To.save()
    NEWO=Webpage.objects.get_or_create(topic_name=To,name=n,url=u,emali=e)[0]
    NEWO.save()
    return HttpResponse('webpage is create')








