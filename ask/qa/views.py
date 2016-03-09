from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def test(request, *args, **kwargs):
    return HttpResponse('OK')

def category_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    pk = args[0]
    return HttpResponse(pk+'OK')

def post_detail(request, *args, **kwargs):
    print(args)
    print(kwargs)
    pk = kwargs['pk']
    print('pk=',pk)
    return HttpResponse(pk+'OK')

def article(request, *args):
    pk = args[0]
    print(pk)
    return HttpResponse(pk+'OK')

#def post_detail(request, pk=None):

#    print('pk==',pk)
 #   return HttpResponse(pk+'OK')