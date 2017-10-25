# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def index(request):
    print "Main Page!"
    return render(request,'pages/index.html')

def sub_index(request):
    print "Sub Page!"
    return render(request,'pages/sub.html')
