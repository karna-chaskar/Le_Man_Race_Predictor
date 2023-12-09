import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge

model = pickle.load(open('Ridge_lap.sav','rb'))
Le_Man_dict = pickle.load(open('Le_Man_dict.pkl','rb'))
Le_Man = pd.DataFrame(Le_Man_dict)

st.title('Le Mans Lap Time Prediction')
# st.image('le_man_Poster.jpg')

def user_report():
    team = st.selectbox('Teams',Le_Man['Team'].unique())

    # Filter drivers based on the selected team
    filtered_drivers = Le_Man.loc[Le_Man['Team'] == team, 'Drivers'].unique()
    driver = st.selectbox('Drivers', filtered_drivers)

    # Filter Cars based on the selected team
    filtered_car = Le_Man.loc[Le_Man['Team'] == team, 'Car'].unique()
    car = st.selectbox('Car', filtered_car)

    # Filter Category based on the selected team
    filtered_category = Le_Man.loc[Le_Man['Team'] == team, 'Category'].unique()
    category = st.selectbox('Category', filtered_category)

    # Filter tyres based on the selected team
    filtered_tyres = Le_Man.loc[Le_Man['Team'] == team, 'Tyres  '].unique()
    tyres = st.selectbox('Tyres', filtered_tyres)

    pitstop = st.selectbox('Pitstops', Le_Man['Pitstops'].unique())

    speed = st.selectbox('Speed', Le_Man['Best Lap Kph'].unique())

    user_report_data = {
    'Team': team,
    'Drivers':driver,
    'Car':car,
    'Category':category,
    'Tyres  ':tyres,
    'Pitstops':pitstop,
    'Best Lap Kph':speed
    }
    report_data = pd.DataFrame(user_report_data, index=[0])
    return report_data

user_data = user_report()
st.header('Reports')
st.write(user_data)

time = model.predict(user_data)
st.subheader('Lap Time in Seconds')
st.subheader(str(round(time[0],1)))
