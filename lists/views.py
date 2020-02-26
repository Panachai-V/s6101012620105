from django.shortcuts import render
from django.template import Context,loader,RequestContext
from django.forms import ModelForm
from django.http import HttpResponse, Http404,HttpResponseRedirect,HttpResponseNotFound
# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def add(request):
    res = 0
    if request.method == 'POST':
        val1 = int(request.POST['num1'])
        val2 = int(request.POST['num2'])

        res = val1 + val2
    return render(request,'home.html',{'result': res})