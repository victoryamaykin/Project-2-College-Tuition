#!/usr/bin/env python
# coding: utf-8


import plotly.plotly as py
import plotly.graph_objs as go 
import json
import folium
from datetime import datetime
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


df = pd.read_csv('data/sample.csv')
df.columns = [col.replace('nan', '') for col in df.columns]




#convert dataframe to numeric
df = df.convert_objects(convert_numeric=True)
df.head()




#Greeen
trace_high = go.Scatter(x=list(df.State),
                        y=list(df.privateTotal),
                        name='privateTotal',
                        line=dict(color='#008000'))




trace_high_avg = go.Scatter(x=list(df.State),
                            y=[df.privateTotal.mean()]*len(df.State),
                            name='privateTotal Average',
                            visible=False,
                            line=dict(color='#008000', dash='dash'))




#maroon
trace_low = go.Scatter(x=list(df.State),
                       y=list(df.public4Year_total),
                       name='public4Year_total',
                       line=dict(color='#800000'))




trace_low_avg = go.Scatter(x=list(df.State),
                           y=[df.public4Year_total.mean()]*len(df.State),
                           name='public4Year_total Average',
                           visible=False,
                           line=dict(color='#800000', dash='dash'))




#public4Year_outState navy
trace_low2 = go.Scatter(x=list(df.State),
                       y=list(df.public4Year_outStateTotal),
                       name='public4Year_outStateTotal',
                       line=dict(color='#000080'))




trace_low2_avg = go.Scatter(x=list(df.State),
                           y=[df.public4Year_outStateTotal.mean()]*len(df.State),
                           name='public4Year_outStateTotal Average',
                           visible=False,
                           line=dict(color='#000080', dash='dash'))




#public2YInState black
trace_low3 = go.Scatter(x=list(df.State),
                        y=list(df.public2YInState),
                        name='public2YInState',
                        line=dict(color='#000000'))




trace_low3_avg = go.Scatter(x=list(df.State),
                            y=[df.public2YInState.mean()]*len(df.State),
                            name='public2YInState Average',
                            visible=False,
                            line=dict(color='#000000', dash='dash'))




data = [trace_high, trace_high_avg, trace_low, trace_low_avg, trace_low2, trace_low2_avg,trace_low3, trace_low3_avg]



high_annotations=[dict(x='State',
                       y=df.privateTotal.mean(),
                       xref='x', yref='y',
                       text='privateTotal Average:<br>'+str(df.privateTotal.mean()),
                       ax=0, ay=-40),
                  dict(x=df.privateTotal.idxmax(),
                       y=df.privateTotal.max(),
                       xref='x', yref='y',
                       text='privateTotal Max:<br>'+str(df.privateTotal.max()),
                       ax=0, ay=-40)]




low_annotations=[dict(x='State',
                      y=df.public4Year_total.mean(),
                      xref='x', yref='y',
                      text='public4Year_total Average:<br>'+str(df.public4Year_total.mean()),
                      ax=0, ay=40),
                 dict(x=df.privateTotal.idxmin(),
                      y=df.public4Year_total.min(),
                      xref='x', yref='y',
                      text='public4Year_total Min:<br>'+str(df.public4Year_total.min()),
                      ax=0, ay=40)]




low2_annotations=[dict(x='State',
                      y=df.public4Year_outStateTotal.mean(),
                      xref='x', yref='y',
                      text='public4Year_outStateTotal Average:<br>'+str(df.public4Year_outStateTotal.mean()),
                      ax=0, ay=40),
                 dict(x=df.privateTotal.idxmin(),
                      y=df.public4Year_outStateTotal.min(),
                      xref='x', yref='y',
                      text='public4Year_outStateTotal Min:<br>'+str(df.public4Year_outStateTotal.min()),
                      ax=0, ay=40)]




low3_annotations=[dict(x='State',
                       y=df.public2YInState.mean(),
                       xref='x', yref='y',
                       text='public2YInState Average:<br>'+str(df.public2YInState.mean()),
                       ax=0, ay=-40),
                  dict(x=df.privateTotal.idxmax(),
                       y=df.public2YInState.max(),
                       xref='x', yref='y',
                       text='public2YInState Max:<br>'+str(df.public2YInState.max()),
                       ax=0, ay=-40)]




updatemenus = list([
    dict(active=-1,
         buttons=list([   
            dict(label = 'privateTotal',
                 method = 'update',
                 args = [{'visible': [True, True, False, False,False,False,False,False]},
                         {'title': 'Tuition High',
                          'annotations': high_annotations}]),
            dict(label = 'public4Year_total',
                 method = 'update',
                 args = [{'visible': [False, False, True, True,False,False,False,False]},
                         {'title': 'Tuition Low',
                          'annotations': low_annotations}]),
             dict(label = 'public4Year_outStateTotal',
                 method = 'update',
                 args = [{'visible': [False, False, False, False,True,True,False,False]},
                         {'title': 'Tuition Low2',
                          'annotations': low2_annotations}]),
             dict(label = 'public2YInState',
                 method = 'update',
                 args = [{'visible': [False, False, False, False,False,False,True,True]},
                         {'title': 'Tuition 2YearIn',
                          'annotations': low3_annotations}]),
            dict(label = 'Both',
                 method = 'update',
                 args = [{'visible': [True, False, True, False,True,False,True,False]},
                         {'title': 'Tuition',
                          'annotations': high_annotations+low_annotations+low2_annotations+low3_annotations}]),
            dict(label = 'Reset',
                 method = 'update',
                 args = [{'visible': [True, False, True, False,True,False,True,False]},
                         {'title': 'Tuition',
                          'annotations': []}])
        ]),
    )
])




layout = dict(title='Tuition', showlegend=True,
              updatemenus=updatemenus)

fig = dict(data=data, layout=layout)
py.iplot(fig, filename='update_dropdown')




with open ('data/us-states.json') as f:
    map_data = json.load(f)
#sns.heatmap(students.dropna())
#print(map_data)
#students = pd.read_csv('data/sample.csv')
students = df


students_map = folium.Map(location=[48, -102], zoom_start=3)

students_map.choropleth(
    geo_data=map_data,
    name='choropleth',
    data=students,
    columns=['State',"privateTotal"],
    key_on='id',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='cost of school by State'
)


folium.LayerControl().add_to(students_map)
students_map.save('map_student.html')

students_map

