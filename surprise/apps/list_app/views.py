# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "list_app/index.html")

def display(request):
    counts = request.POST['number']
    item = ""
    arr = []
    for i in range(0,int(counts)):
        item = "Item " + str(i+1)
        arr.append(item)
    context = {
        "result": '\n'.join(arr)
    }
    print context
    return render(request, "list_app/display.html",context)
