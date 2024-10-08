import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier


st.title(' 🌦 Weather Prediction ⛈')

st.info(' This Machine learning Model predicts the weather')

with st.expander('Data'):
  st.write("Weather data")
  weather=pd.read_csv("https://raw.githubusercontent.com/GEETHESWARI/Weather_pred/refs/heads/main/seattle-weather.csv")
  weather

  st.write('**X**')
  X_raw = weather.drop(['weather','date'], axis=1)
  X_raw

  st.write('**y**')
  y_raw = weather.weather
  y_raw

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
  precipitation= st.slider("Precipitation",0.0,3.5,56.5)
  temp_max= st.slider("Maximun Temperature",-1.0,16.5,36.2)
  temp_min= st.slider("Minimun Temperature",-7.0,7.5,18.8)
  wind= st.slider("Wind Speed ",0.0,3.4,10.2)
  
  data={'precipitation': precipitation, 
        'temp_max': temp_max,
        'temp_min': temp_min,
        'wind':wind}
  input_df=  pd.DataFrame(data, index=[0])
  input_weather = pd.concat([input_df, X_raw], axis=0)


with st.expander('Input features'):
  st.write('**Input Weather features**')
  input_df
  st.write('**Combined  data**')
  input_weather



df_weather = pd.get_dummies(input_weather)

X = df_weather[1:]
input_row = df_weather[:1]

# Encode y
target_mapper = {'drizzle': 0, 
                 'rain': 1,
                 'sun': 2,
                 'snow': 3, 
                 'fog':4 }

def target_encode(val):
  return target_mapper[val]

y = y_raw.apply(target_encode)

with st.expander('Data preparation'):
  st.write('**Encoded X (input Weather )**')
  input_row
  st.write('**Encoded y**')
  y


# Model training and inference
## Train the ML model
clf = RandomForestClassifier()
clf.fit(X, y)

## Apply model to make predictions
prediction = clf.predict(input_row)
prediction_proba = clf.predict_proba(input_row)

df_prediction_proba = pd.DataFrame(prediction_proba)
df_prediction_proba.columns = ['drizzle', 'rain', 'sun', 'snow', 'fog']
df_prediction_proba.rename(columns={0: 'drizzle',
                                       1: 'rain' ,
                                       2: 'sun',
                                       3: 'snow', 
                                       4: 'fog'})


st.subheader('Predicted Weather')
# Display the dataframe in the first row
with st.container():
    st.dataframe(df_prediction_proba[['drizzle', 'rain']], column_config={
        'drizzle': st.column_config.ProgressColumn(
            'drizzle',
            format='%f',
            width='medium',
            min_value=0,
            max_value=1
        ),
        'rain': st.column_config.ProgressColumn(
            'rain',
            format='%f',
            width='medium',
            min_value=0,
            max_value=1
        )
    }, hide_index=True)

# Display the dataframe in the second row
with st.container():
    st.dataframe(df_prediction_proba[['sun', 'snow']], column_config={
        'sun': st.column_config.ProgressColumn(
            'sun',
            format='%f',
            width='medium',
            min_value=0,
            max_value=1
        ),
        'snow': st.column_config.ProgressColumn(
            'snow',
            format='%f',
            width='medium',
            min_value=0,
            max_value=1
        )
    }, hide_index=True)

# Display the dataframe in the third row
with st.container():
    st.dataframe(df_prediction_proba[['fog']], column_config={
        'fog': st.column_config.ProgressColumn(
            'fog',
            format='%f',
            width='medium',
            min_value=0,
            max_value=1
        )
    }, hide_index=True)

weather_pred = np.array(['drizzle', 'rain', 'sun', 'snow', 'fog'])
st.success(str(weather_pred[prediction][0]))
  
  
  

 
 
  
