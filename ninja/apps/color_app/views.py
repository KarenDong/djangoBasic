# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def index(request):
    return render(request,"color_app/index.html")

def ninja(request):
    context = {
        "ninjas": True
    }
    return render(request,"color_app/show.html", context)

def colors(request,ninja_color):
    context = {
        "color": ninja_color,
        "ninjas": False
    }
    print context
    return render(request,"color_app/show.html", context)
