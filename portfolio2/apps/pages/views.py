# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def index(request):
    print "Main page!"
    return render(request,'pages/index.html')

def projects(request):
    print "Project page!"
    return render(request,'pages/projects.html')

def about(request):
    print "About ME!"
    return render(request,'pages/about.html')

def testmimonials(request):
    print "Testmimonials page!"
    return render(request,'pages/testmimonials.html')
