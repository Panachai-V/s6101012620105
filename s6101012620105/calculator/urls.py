from django.conf.urls import url
from . import views
app_name = "calculator"
urlpatterns = [

    url(r'^$', views.index, name =  "index"),
    #127.0.0.1/calculator/
    url(r'^(?P<question_id>[0-9]+)/$',views.detail,name="detail"),
    #127.0.0.1/calculator/1
    url(r'^(?P<question_id>[0-9]+)/results$',views.results,name="results"),
    #127.0.0.1/calculator/1/results
    url(r'^(?P<question_id>[0-9]+)/vote$',views.vote,name="vote"),
    #127.0.0.1/calculator/1/vote
]
