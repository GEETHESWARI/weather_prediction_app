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
  st.write("**Weather data info**")
  st.write("*Weather data shape & size*")
  
  weather.shape
  weather.size
  st.write("*INFO*")
  print(weather.info())
  st.write("*Describe*")
  weather.describe()
  st.write("*Checking Null Values*")
  weather.isnull().sum()
  st.write("*Value Counts of Target Variables*")
  weather.weather.value_counts()
  
