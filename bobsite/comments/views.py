from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import bobsite.settings as set
from .forms import CommentForm
# Create your views here.

def comments(request):
     return( render(request,set.TEMPLATE_DIRS[1]+'/index.html',{"form":CommentForm}))
