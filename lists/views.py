from django.shortcuts import render
from django.template import Context,loader,RequestContext
from django.forms import ModelForm
from django.http import HttpResponse, Http404,HttpResponseRedirect,HttpResponseNotFound
from lists.models import cal_his,get_his,post_his
# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def home_POST(request):
    return render(request, 'home_POST.html')

def home_GET(request):
    return render(request, 'home_GET.html')

def operate_post(request):
    res = 0
    if request.method == 'POST':
        val1 = float(request.POST['num1'])
        val2 = float(request.POST['num2'])
        if 'add' in request.POST:
            res = val1 + val2
            op = '+'
            post_his.objects.create(x_value = val1, y_value = val2, op_value =op, res_value = res)
            post_his_list = post_his.objects.all()
            return render(request,'home_POST.html',{'result': post_his_list})
        elif 'sub' in request.POST:
            res = val1 - val2
            op = '-'
            post_his.objects.create(x_value=val1, y_value=val2, op_value=op, res_value=res)
            post_his_list = post_his.objects.all()
            return render(request,'home_POST.html',{'result': post_his_list})
        elif 'mul' in request.POST:
            res = val1 * val2
            op = '*'
            post_his.objects.create(x_value=val1, y_value=val2, op_value=op, res_value=res)
            post_his_list = post_his.objects.all()
            return render(request,'home_POST.html',{'result': post_his_list})
        elif 'div' in request.POST:
            res = val1 / val2
            op = '/'
            post_his.objects.create(x_value=val1, y_value=val2, op_value=op, res_value=res)
            post_his_list = post_his.objects.all()
            return render(request,'home_POST.html',{'result': post_his_list})


def operate_get(request):
    res = 0
    if request.method == 'GET':
        val1 = float(request.GET['num1'])
        val2 = float(request.GET['num2'])
        if 'add' in request.POST:
            res = val1 + val2
            op = '+'
            get_his.objects.create(x_value = val1, y_value = val2, op_value =op, res_value = res)
            get_his_list = get_his.objects.all()
            return render(request,'home_POST.html',{'result': get_his_list})
        elif 'sub' in request.POST:
            res = val1 - val2
            op = '-'
            get_his.objects.create(x_value=val1, y_value=val2, op_value=op, res_value=res)
            get_his_list = post_his.objects.all()
            return render(request,'home_POST.html',{'result': get_his_list})
        elif 'mul' in request.POST:
            res = val1 * val2
            op = '*'
            get_his.objects.create(x_value=val1, y_value=val2, op_value=op, res_value=res)
            get_his_list = post_his.objects.all()
            return render(request,'home_POST.html',{'result': get_his_list})
        elif 'div' in request.POST:
            res = val1 / val2
            op = '/'
            get_his.objects.create(x_value=val1, y_value=val2, op_value=op, res_value=res)
            get_his_list = get_his.objects.all()
            return render(request,'home_POST.html',{'result': get_his_list})
