from django.shortcuts import render
# from django.http import HttpResponse

def index(request):
    x = {'name':'rida', 'age':'23'}
    return(render(request, 'index.html', x))
    # return(HttpResponse('Hello World'))
    # return(render())
# Create your views here.

def Tags(request):
    xx = {'name':'rida', 'age':'23'}
    return(render(request, 'Tags.html', xx))
def Tags1(request):
      return(render(request, 'Tags1.html'))
def Tags2(request):
        return(render(request, 'Tags2.html'))
