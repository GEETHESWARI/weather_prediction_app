import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


st.title(' 🌦 Weather Prediction ⛈')

st.info(' This Machine learning Model predicts the weather')

with st.expander('Data'):
  st.write("Weather data")
  weather=pd.read_csv("https://raw.githubusercontent.com/GEETHESWARI/Weather_pred/refs/heads/main/seattle-weather.csv")
  weather

with st.expander('Data Visualization'):
  st.area_chart(
    weather,
    x="date",
    y=["temp_max"],
    color="weather",
    stack="center")

  fig_wind = px.scatter(weather, x='wind',y="precipitation",color="weather")
  temp_max=px.scatter(data_frame=weather,x='temp_max',y="temp_min",color="weather",color_continuous_scale="reds")
  date_= px.scatter_matrix(weather,dimension=['precipitation', 'temp_max', 'temp_min', 'wind'],color='weather',line_group="weather")

  
  tab1,tab2,tab3=st.tabs(["Wind Vs Precipitation","Temp_max Vs Temp_min","Date Vs Temp_max"])
  with tab1:
   st.plotly_chart(fig_wind, theme=None,use_container_width=True)
  with tab2:  
   st.plotly_chart(temp_max, theme=None,use_container_width=True)
  with tab3:
    st.plotly_chart(date_, theme=None,use_container_width=True)
  
  

 
 
  
