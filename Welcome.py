import streamlit as st
import pandas as pd
from bokeh.plotting import figure
# from bokeh.io import output_notebook
# import matplotlib.pyplot as plt
import os

file_name_list = []
for i in os.listdir():
  if i.endswith('csv'):
    file_name_list.append(i)

st.write('Hello World')

df = pd.read_csv('Bastar Craton.csv')
st.dataframe(df)

# file_name = st.multiselect('select location', file_name_list, file_name_list[0])
file_name = st.selectbox('select location', file_name_list)
df = pd.read_csv(file_name)

el_list = df.columns.tolist()[27:80]
x_axis = st.selectbox('select x axis', el_list)
y_axis = st.selectbox('select y axis', el_list)

x = df[x_axis]/10000 
y = df[y_axis]/10000

p = figure(
    x_axis_label=x_axis,
    y_axis_label=y_axis)

p.circle(x, y)

st.bokeh_chart(p, use_container_width=True)
