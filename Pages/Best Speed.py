import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

model = pickle.load(open('RandomForest_kph.sav','rb'))
Le_Man_dict = pickle.load(open('Le_Man_dict.pkl','rb'))
Le_Man = pd.DataFrame(Le_Man_dict)

st.title('Le Mans Lap Time Prediction')
# st.image('le_man_Poster.jpg')

def user_report():
    car = st.selectbox('Car',Le_Man['Car'].unique())

    # Filter Car No based on the selected Car
    filtered_car_no = Le_Man.loc[Le_Man['Car'] == car, 'Car No.'].unique()
    car_no = st.selectbox('Cars', filtered_car_no)

    # Filter Category based on the selected Car
    filtered_category = Le_Man.loc[Le_Man['Car'] == car, 'Category'].unique()
    category = st.selectbox('Category', filtered_category)

    # Filter Tyres based on the selected Car
    filtered_tyres = Le_Man.loc[Le_Man['Car'] == car, 'Tyres  '].unique()
    tyres = st.selectbox('Tyres', filtered_tyres)

    lap = st.selectbox('Laps', Le_Man['Laps'].unique())

    pitstop = st.selectbox('Pitstops', Le_Man['Pitstops'].unique())


    user_report_data = {
    'Car': car,
    'Car No.':car_no,
    'Category':category,
    'Tyres  ':tyres,
    'Laps':lap,
    'Pitstops':pitstop,
    }

    report_data = pd.DataFrame(user_report_data, index=[0])
    return report_data

user_data = user_report()
st.header('Reports')
st.write(user_data)

best_speed = model.predict(user_data)
best_speed = np.expm1(best_speed)

st.subheader('Speed of Car')
# Format the result
speed_string = str(round(best_speed[0],1))
result = f"{speed_string} Kph "

st.subheader(result)
