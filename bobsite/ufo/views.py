from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import bobsite.settings as set
from .forms import UserForm

# Create your views here.
def index(request):
	 print("in views TEMPLATE_DIRS = {}".format(set.TEMPLATE_DIRS))
	 return( render(request,'index.html'))
