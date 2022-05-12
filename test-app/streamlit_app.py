import streamlit as st
import pandas as pd

st.title("My First Streamlit Web App")

df = pd.read_csv('dataset.csv')
st.write(df)
