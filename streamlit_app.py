import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

st.title(' 🌦 Weather Prediction ⛈')

st.info(' This Machine learning Model predicts the weather')

with st.expander('Data'):
  st.write("Weather data")
  weather=pd.read_csv("https://raw.githubusercontent.com/GEETHESWARI/Weather_pred/refs/heads/main/seattle-weather.csv")
  weather

with st.expander('Data Visualization'):
  st.scatter_chart(
    weather,
    x="date",
    y=["temp_max", "temp_min"],
    size="weather")
 
  
