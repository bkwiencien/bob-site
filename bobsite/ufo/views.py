from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import bobsite.settings as set

# Create your views here.
def index(request):
	 #return render(request, 'polls/detail.html')
	 print("in views TEMPLATE_DIRS = {}".format(set.TEMPLATE_DIRS))
	 #return render(request, set.TEMPLATE_DIRS[0]+'templates/index.html')
	 return( render(request,'index.html'))
