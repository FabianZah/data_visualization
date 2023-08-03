import streamlit as st
import pandas as pd
import numpy as np
from bokeh.plotting import figure
import os

file_name_list = []
for i in os.listdir():
  if i.endswith('csv'):
    file_name_list.append(i)
    
tab1, tab2, tab3 = st.tabs(["Hello world", "Dataframe", "Interactive plot"])

with tab1:
  st.write('Hello World')
  
with tab2:
  df = pd.read_csv('Bastar Craton.csv')
  st.dataframe(df)
  
with tab3:
  col1, col2 = st.columns(2)
  
  with col1:
    st.header("Selection")
    # file_name = st.multiselect('select location', file_name_list, file_name_list[0])
    file_name = st.selectbox('select location', file_name_list)
    df = pd.read_csv(file_name)
    
    el_list = df.columns.tolist()[27:80]
    x_axis = st.selectbox('select x axis', el_list)
    y_axis = st.selectbox('select y axis', el_list)
  with col2:
    st.header('Plot of your selection')
    x = df[x_axis]/10000 
    y = df[y_axis]/10000
    x_min = np.min(df[x_axis]/10000)
    x_max = np.max(df[x_axis]/10000)
    y_mean = np.mean(df[y_axis]/10000)
    y_std = np.std(df[y_axis]/10000)
                   
    genre = st.radio(
      "Choose the standard deviation range to plot",
      ('1SD', '2SD', '3SD'))
         
    p = figure(x_axis_label=x_axis, y_axis_label=y_axis)
    
    p.circle(x, y)
    p.line([x_min-2, x_max+2],[y_mean,y_mean], line_width = 2)
  
    if genre == '1SD':
      p.line([x_min-2, x_max+2],[y_mean-y_std,y_mean-y_std], line_width = 1.5, line_color = 'gray')
      p.line([x_min-2, x_max+2],[y_mean+y_std,y_mean+y_std], line_width = 1.5, line_color = 'gray')
         
    elif genre == '2SD':
      p.line([x_min-2, x_max+2],[y_mean-2*y_std,y_mean-2*y_std], line_width = 1.5, line_color = 'gray')
      p.line([x_min-2, x_max+2],[y_mean+2*y_std,y_mean+2*y_std], line_width = 1.5, line_color = 'gray')
    elif genre == '3SD':
      p.line([x_min-2, x_max+2],[y_mean-3*y_std,y_mean-3*y_std], line_width = 1.5, line_color = 'gray')
      p.line([x_min-2, x_max+2],[y_mean+3*y_std,y_mean+3*y_std], line_width = 1.5, line_color = 'gray')
    else:
      st.write('Choose a proper SD')

    
    st.bokeh_chart(p, use_container_width=True)
