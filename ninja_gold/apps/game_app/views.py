# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from datetime import datetime
from random import *

def index(request):
    print "Game Start"
    request.session['time'] = str(datetime.now())
    return render(request,'game_app/index.html')

def games(request):
    try:
        request.session['total_gold']
    except:
        request.session['total_gold'] = 0

    request.session['building'] = request.POST['building']

    if request.session['building'] == "casino":
        request.session['gold'] = randint(-50,50)
        if request.session['gold'] > 0:
            request.session['display'] = 1
        else:
            request.session['display'] = 2
    elif request.session['building'] == "farm":
        request.session['gold'] = randint(10,20)
        request.session['display'] = 1
    elif request.session['building'] == "cave":
        request.session['gold'] = randint(5,10)
        request.session['display'] = 1
    elif request.session['building'] == "house":
        request.session['gold'] = randint(2,5)
    request.session['total_gold'] += request.session['gold']
    return redirect('/')
