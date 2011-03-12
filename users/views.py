# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings
from django.template import RequestContext

def index(request):
    return render_to_response("users/index.html")
