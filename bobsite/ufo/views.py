from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import bobsite.settings as set
from .forms import UserForm
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
import io
import pdb
import base64


# Create your views here.
def index(request):
     dict = {"form":UserForm}
     return( render(request,'index.html',context=dict))
def fetch_year(x):
    return(x.split('/')[2].split(" ")[0]) 
def fetch_date(x):
    day_dict={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thurdday',5:'Friday',6:'Saturday'}
    return(day_dict[pd.to_datetime(x).weekday()])
def genbarchart(request):
    plt.switch_backend('agg')
    dictstatus = {"status":"no data for that timeframe"}
    state = request.POST['your_state']
    year  = request.POST['your_year']
    df = pd.read_csv('http://bit.ly/uforeports')
    df = df[df.State==state]
    if (year != 'ALL Years'):
      df['Year'] = df['Time'].apply(fetch_year)
      df = df[df.Year==year]
      df['Day_of_week'] = df['Time'].apply(fetch_date)
    t = df['Shape Reported'].value_counts()
    fig = plt.figure()
    numb = tuple(t.values)
    plt.rcParams["figure.figsize"] = [len(numb),len(numb)]
    #pdb.set_trace()
    categories = tuple(t.index)
    #numb = tuple(t.values)
    y_pos = np.arange(len(categories))
    plt.xticks(y_pos, categories,rotation='vertical')
    plt.bar(y_pos, numb, align='center', alpha=0.5,width=.1)
    f = io.BytesIO()
    fig.savefig(f,format='png',bbox_inches='tight')
    f.seek(0)
    image=base64.b64encode(f.getvalue())
    image=str(image,'utf-8')
    if (year != 'ALL Years'):
      df['Year'] = df['Time'].apply(fetch_year)
      df = df[df.Year==year]
      df['Day_of_week'] = df['Time'].apply(fetch_date)
    if (df.size != 0):
      df['Year'] = df['Time'].apply(fetch_year)
      df['Day_of_week'] = df['Time'].apply(fetch_date)
      l_dict = {"listo":df.to_html()}
      #pdb.set_trace()
      return render(request,"index.html",{"listo":df.to_html,'charto':image})
    else:
       return (render(request,"index.html",context=dictstatus)) 