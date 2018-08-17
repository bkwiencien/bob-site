from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import bobsite.settings as set
from .forms import CommentForm
from .models import Comments
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def comments(request):
     return( render(request,set.TEMPLATE_DIRS[1]+'/index.html',{"form":CommentForm}))
@csrf_exempt     
def getcomment(request):
     commento = request.POST.get('comment') 
     nameo    = request.POST.get('your_name')
     print('in the view !!!!!!!!!!!!!!!!!!!!!! ' + commento + " " + nameo)
     p = Comments(comment=commento,name=nameo)
     p.save()
     return((render(request,set.TEMPLATE_DIRS[1]+'/thanks.html')))
