# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "first_app/index.html")

def show(request, color):
    print color

    context ={
    'url':"first_app/images/ninjas.jpg"
    }
    if color == "purple":
        context['url']="first_app/images/donnie.jpg"

    elif color == "red":
        context['url']="first_app/images/raph.jpg"

    elif color == "blue":
        context['url']="first_app/images/leo.jpg"

    elif color == "orange":
        context['url']="first_app/images/mikey.jpg"

    elif color == "brown":
        context['url']="first_app/images/mastersplinter.jpg"

    elif color == "":
        pass
        
    else:
        context['url']="first_app/images/april.png"



    return render(request, "first_app/display.html", context)
