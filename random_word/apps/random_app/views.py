# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random
import string

def index(request):
    return render(request,'random_app/index.html')

def create(request):
    try:
        request.session['times'] += 1
    except:
        request.session['times'] = 0

    words = ''
    for i in range(1,14):
        words = words + str(random.choice(string.ascii_letters))
    request.session['str'] = words
    return redirect("/")
