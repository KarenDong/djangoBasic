# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

from datetime import datetime

def index(request):
    print datetime.now()
    context = {
    "times":datetime.now()
    }
    return render(request,'time_app/index.html',context)
# Create your views here.
