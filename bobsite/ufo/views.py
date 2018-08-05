from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import bobsite.settings as set
from .forms import UserForm
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

# Create your views here.
def index(request):
     print("in views TEMPLATE_DIRS = {}".format(set.TEMPLATE_DIRS))
     dict = {"form":UserForm}
     return( render(request,'index.html',context=dict))
def getdata(request):
    dict1 = {"form":UserForm}
    dictstatus = {"status":"No data for that time period"}
    state = request.POST['your_state']
    year  = request.POST['your_year']
    df = pd.read_csv('http://bit.ly/uforeports')
    df = df[df.State==state]
    if (year != 'ALL Years'):
      df['Year'] = df['Time'].apply(fetch_year)
      df = df[df.Year==year]
      df['Day_of_week'] = df['Time'].apply(fetch_date)
    if (df.size != 0):
      df['Year'] = df['Time'].apply(fetch_year)
      df['Day_of_week'] = df['Time'].apply(fetch_date)
      l_dict = {"listo":df.to_html()}
      grouped = gen_bar_chart(df)
      print(grouped)
      return render(request,"index.html",{"listo":df.to_html,"charto":grouped})
    else:
       return (render(request,"index.html",context=dictstatus))  
def fetch_year(x):
    return(x.split('/')[2].split(" ")[0]) 
def fetch_date(x):
    day_dict={0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thurdday',5:'Friday',6:'Saturday'}
    return(day_dict[pd.to_datetime(x).weekday()])
def gen_bar_chart(frame):
    t = frame['Shape Reported'].value_counts()
    fig = Figure()
    canvas = FigureCanvas(fig)
    objects = t.index
    y_pos = np.arange(len(objects))
    performance = t.values
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    response=HttpResponse(content_type='image/png')
    canvas.print_png(response)
    print("about to return from gen_bar_chart ")
    return response   
