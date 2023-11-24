from django.shortcuts import render
import random

def index_pp1(request):
    return render(request, "index_pp1.html")

def maxmin(request):
    n1= random.randint(1,10)
    n2= random.randint(1,10)
    context={
        'n1' : n1,
        'n2' : n2,
        'somma' : n1+n2,
    }
    return render(request, "maxmin.html", context)

def media(request):
    lista=[]
    tot=0
    media=0
    for i in range(30):
        lista.append(random.randint(1,10))
        tot+=lista[i]
    media=tot/30
    context={
        'list' : lista,
        'media' : media,
    }
    return render(request, "media.html", context)

def voti(request):
    context={
        'diz':{'studente1':8, 'studente2':7, 'studente3':5, 'studente4':6, },
    }
    return render(request, "voti.html", context)
    
