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
def gen_day_of_week(frame):
    fig = plt.figure()
    numb = tuple(frame.values)
    plt.rcParams["figure.figsize"] = [5,5]
    plt.rcParams['font.family'] = 'sans-serif'
    plt.title("ditribution of ufo reports by day of week")
    dayname = tuple(frame.index)
    y_pos = np.arange(len(dayname))
    plt.xticks(y_pos, dayname,rotation='vertical')
    plt.bar(y_pos, numb, align='center', alpha=0.5,width=.1)
    f = io.BytesIO()
    fig.savefig(f,format='png',bbox_inches='tight')
    f.seek(0)
    image=base64.b64encode(f.getvalue())
    image=str(image,'utf-8')
    return(image)    
def genbarchart(request):
    plt.switch_backend('agg')
    dictstatus = {"status":"no data for that timeframe"}
    state = request.POST['your_state']
    year  = request.POST['your_year']
    df = pd.read_csv('http://bit.ly/uforeports')
    df = df[df.State==state]
    df['Year'] = df['Time'].apply(fetch_year)
    if (year != 'ALL Years'):
     df = df[df.Year==year]
    df['Day_of_week'] = df['Time'].apply(fetch_date)
    t = df['Shape Reported'].value_counts()
    tt = df['Day_of_week'].value_counts();
    weekday_image = gen_day_of_week(tt)
    fig = plt.figure()
    numb = tuple(t.values)
    plt.rcParams["figure.figsize"] = [len(numb),len(numb)]
    plt.rcParams['font.family'] = 'sans-serif'
    plt.title("ditribution of ufo shapes "+ state)
    #pdb.set_trace()
    categories = tuple(t.index)
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
      return render(request,"dataview.html",{"listo":df.to_html,'chartdayoweek':weekday_image,'charto':image})
    else:
       return (render(request,"index.html",context=dictstatus)) 