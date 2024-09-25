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
  

  fig_wind = px.scatter(weather, x='wind',y="precipitation",color="weather")
  temp_max=px.scatter(data_frame=weather,x='temp_max',y="temp_min",color="weather",color_continuous_scale="reds")
  pair= px.scatter_matrix(weather,dimensions=['precipitation', 'temp_max', 'temp_min', 'wind'],color='weather')
  date_= px.scatter(weather, x='date', y='temp_max',color='weather',symbol="weather",hover_name="weather")
  
  
  tab1,tab2,tab3,tab4=st.tabs(["Wind Vs Precipitation","Temp_max Vs Temp_min","Pair Plots","Date Vs Temp_max"])
  with tab1:
   st.plotly_chart(fig_wind, theme=None,use_container_width=True)
  with tab2:  
   st.plotly_chart(temp_max, theme=None,use_container_width=True)
  with tab3:
    st.plotly_chart(pair, theme=None,use_container_width=True)
  with tab4:
    st.plotly_chart(date_, theme=None,use_container_width=True) 

with st.sidebar:
  st.header("Input Features")
  precipitation= st.slider("Precipitation",0,3,56)
  temp_max= st.slider("Maximun Temperature",-1,16,36)
  temp_min= st.slider("Minimun Temperature",-7,7,18)
  wind= st.slider("Wind Speed ",0,3,10)

  
  
  

 
 
  
