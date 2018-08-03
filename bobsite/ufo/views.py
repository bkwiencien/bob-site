from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import bobsite.settings as set
from .forms import UserForm
import pandas as pd

# Create your views here.
def index(request):
     print("in views TEMPLATE_DIRS = {}".format(set.TEMPLATE_DIRS))
     dict = {"form":UserForm}
     return( render(request,'index.html',context=dict))
def getdata(request):
    dict1 = {"form":UserForm}
    state = request.POST['your_state']
    year  = request.POST['your_year']
   # type  = request.POST['your_type']
    df = pd.read_csv('http://bit.ly/uforeports')
    df = df[df.State==state]
    l_dict = {"listo":df.to_html()}
   # print(df)
    return render(request,"index.html",context=l_dict)
    
