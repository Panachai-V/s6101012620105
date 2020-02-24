from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
#from flask import Flask,render_template,request
from django.template import loader, RequestContext
from .models import Question, Choice
# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[0:5]
    context = {'latest_questions': latest_questions}

    return render(request, "calculator/index.html", context)





