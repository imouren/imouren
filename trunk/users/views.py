# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings
from django.template import RequestContext
from django.views.decorators.cache import cache_page

@cache_page(60*60)
def index(request):
    return render_to_response("users/index.html")

def index_xml(request, filename):
    data = {}
    r = render_to_response("users/index.xml", data, mimetype="text/xml")
    return r

