from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def about(request):
  return HttpResponse("Will update later")

#def service(request)


# Create your views here.
