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

def get_user_tweets(request):
    data = 'FAIL'
    if request.is_ajax():
        print('is ajax')
        username = request.GET.get('username', 'None')
        print('username is ' + username)

        ## complete
        from tasks.py import get_tweets
        job = get_tweets(username)
        print(job)
        data = job[1]
    else:
        data = 'Not an ajax request'

    data_dict = {}
    for status in data:
        data_dict["ID"] = status.Id
        data_dict["ScreenName"] = status.ScreenName

    print(data)
    json_data = json.load()
    return HttpResponse(json_data, content_type='application/json')