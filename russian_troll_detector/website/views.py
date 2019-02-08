# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('website/index.html')
    context = {
                }

    return HttpResponse(template.render(context, request))

def get_tweets(request):
    data = 'FAIL'
    if request.is_ajax():
        print('is ajax')
        username = request.GET.get('username', 'None')
        print(username)
    else:
        data = 'Not an ajax request'

    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')