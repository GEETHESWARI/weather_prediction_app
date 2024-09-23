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


weather=pd.read_csv("https://github.com/GEETHESWARI/Weather_pred/blob/main/seattle-weather.csv")

weather
