# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response


def markdown_ref(req):
    return render_to_response('markdown_ref.html')