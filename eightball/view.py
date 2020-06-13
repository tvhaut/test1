from django.http import HttpResponse
from django.shortcuts import render, redirect
from random import randint

def question(request):
    randomGetal = randint(1,20)
    
    f = open("eightball.txt", "r")
    for x in range(randomGetal):
        lijn= f.readline()

    return render(request,"answer.html",{'lijnParam': lijn, 'getal':randomGetal})


