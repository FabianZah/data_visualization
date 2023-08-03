import streamlit as st
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
# import matplotlib.pyplot as plt
import os

file_name_list = []
for i in os.listdir():
  if i.endswith('csv'):
    file_name_list.append(i)

st.write('Hello World')

df = pd.read_csv('Bastar Craton.csv')
st.dataframe(df)

el_list = df.columns.tolist()[27:80]
x_axis = st.selectbox('select element', el_list)

st.multiselect('select location', file_name_list, file_name_list[0])

output_notebook()
p = figure(x_axis_label = 'x', y_axis_label = 'y')
p.circle(df['Mg']/10000,df['Si']/10000)

st.bokeh_chart(p, use_container_width=True)
