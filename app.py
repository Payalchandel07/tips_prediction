
import streamlit as st
import pickle
import pandas as pd
model=pickle.load(open('tips_model.pkl','rb'))
st.title("Tip Prediction app")
total_bill=st.number_input("Total Bill")
size=st.number_input("size")
sex=st.selectbox('sex',['Male','Demale'])
smoker=st.selectbox('smoker',['yes','no'])
day=st.selectbox('day',['Thur','Fri','Sat','Sun'])
time=st.selectbox('time',['Lunch','Dinner'])
input_data=pd.DataFrame({
    "total_bill":[total_bill],
    'size':[size],
    'sex':[sex],
    'smoker':[smoker],
    'day':[day],
    'time':[time]
    })
if st.button('Predict Trip'):
  Prediction=model.predit(input_data)
  st.success(f"predicted Tip:{Prediction[0]:2f}")

