import streamlit as st
import pickle
import pandas as pd

Le_Man_dict = pickle.load(open('Le_Man_dict.pkl','rb'))
Le_Man = pd.DataFrame(Le_Man_dict)

st.set_page_config(
    page_title = 'Select option'
)

st.title('_They Will Be There!_')
st.sidebar.success('select page above')

st.image('Home.jpg')

st.title('2023 Results')

selected_columns = ['Car', 'Car No.', 'Drivers', 'Category', 'Tyres  ', 'Total Time', 'Best Lap Kph']
top_10_cars = Le_Man.sort_values(by='Total Time').drop_duplicates(subset='Car').head(10)[selected_columns]
top_cars = top_10_cars.reset_index()

st.table(top_cars)