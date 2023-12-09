import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor


model = pickle.load(open('RandomForest_time.sav','rb'))
Le_Man_dict = pickle.load(open('Le_Man_dict.pkl','rb'))
Le_Man = pd.DataFrame(Le_Man_dict)

st.title('Total Time Predictor')
# st.image('le_man_Poster.jpg')

def user_report():
    hour = st.selectbox('Hour',Le_Man['Hour'].unique())

    car = st.selectbox('Car',Le_Man['Car'].unique())

    # Filter Car No based on the selected Car
    filtered_car_no = Le_Man.loc[Le_Man['Car'] == car, 'Car No.'].unique()
    car_no = st.selectbox('Cars', filtered_car_no)

    lap = st.selectbox('Laps', Le_Man['Laps'].unique())

    pitstop = st.selectbox('Pitstops', Le_Man['Pitstops'].unique())

    speed = st.selectbox('Speed', Le_Man['Best Lap Kph'].unique())


    user_report_data = {
    'Hour':hour,
    'Car': car,
    'Car No.':car_no,
    'Laps':lap,
    'Pitstops':pitstop,
    'Best Lap Kph':speed,
    }

    report_data = pd.DataFrame(user_report_data, index=[0])
    return report_data

user_data = user_report()
st.header('Reports')
st.write(user_data)

log_time = model.predict(user_data)
time = np.expm1(log_time)

st.subheader('Total Time to cover')

sec = round(time[0],1)
hours = int(sec // 3600)
minutes = int((sec % 3600) // 60)
seconds = sec % 60

# Format the result
duration_string = f"{hours} hr : {minutes} min : {seconds:.2f} sec"

st.subheader(str(duration_string))