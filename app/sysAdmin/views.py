from django.shortcuts import render_to_response

# Create your views here.
# @ensure_csrf_cookie
def index(req):
    return render_to_response('index.html')