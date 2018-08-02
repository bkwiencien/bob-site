from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import bobsite.settings as set
from .forms import UserForm

# Create your views here.
def index(request):
	 print("in views TEMPLATE_DIRS = {}".format(set.TEMPLATE_DIRS))
	 dict = {"form":UserForm}
	 return( render(request,'index.html',context=dict))
def getdata(request):
     return("hello ferret face")
