from django.shortcuts import render
from django.template import Context,loader,RequestContext
from django.forms import ModelForm
from django.http import HttpResponse, Http404,HttpResponseRedirect,HttpResponseNotFound
# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def operate(request):
    res = 0
    if request.method == 'POST':
        val1 = float(request.POST['num1'])
        val2 = float(request.POST['num2'])
        if 'add' in request.POST:
            res = val1 + val2
            return render(request,'home.html',{'result': res})
        elif 'sub' in request.POST:
            res = val1 - val2
            return render(request,'home.html',{'result': res})
        elif 'mul' in request.POST:
            res = val1 * val2
            return render(request,'home.html',{'result': res})
        # elif 'div' in request.POST:
        #     res = val1 / val2
        #     return render(request,'home.html',{'result': res})
