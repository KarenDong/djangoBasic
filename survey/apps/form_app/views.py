# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,'form_app/index.html')
def create(request):
    try:
        request.session['counts'] += 1
    except:
        request.session['counts'] = 1

    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['fav']
    request.session['comment'] = request.POST['comment']

    return render(request,'form_app/result.html')

def runThis(request):
    return redirect('/')
