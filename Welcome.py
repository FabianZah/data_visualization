import streamlit as st
import pandas as pd

st.write('Hello World')

df = pd.read_csv('Emeishan.csv')
st.dataframe('df')
