#ML LIBRARIES/Machine Learning/mini project/solar/solar radiation regression.ipynb
# importing dependencies
import pickle
import streamlit as st

# load model
#Model=pickle.load(open("C:\Users\Rajina Nisar\ML LIBRARIES\Machine Learning\mini project\solar\Model",'rb'))
Model = pickle.load(open(r"C:\Users\Rajina Nisar\ML LIBRARIES\Machine Learning\mini project\solar\Model", 'rb'))
# Header
st.header('Solar Radiation Detection')
# text
st.text('Ckeck how much radiation is get')
st.subheader('')


st.subheader('')
st.text('Fill cells below ')
# creating a 3*3 structure
col1,col2,col3,col4=st.columns(4)
with col1:
    Temperature=st.number_input('Temperature')
    Pressure=st.number_input('Pressure')
    Humidity=st.number_input('Humidity')
with col2:    
    WindDirection_in_Degrees=st.number_input('WindDirection(Degrees)')
    Speed=st.number_input('Speed')
    month=st.number_input('month')
with col3:    
    day=st.number_input('day')
    Hour=st.number_input('Hour')
    Minute=st.number_input('Minute')
with col4:    
    RiseMinute=st.number_input('RiseMinute')
    SetHour=st.number_input('SetHour')
    SetMinute=st.number_input('SetMinute')
    
# Button
#if st.button('Check'):
    #predicted=random_forest.predict([[Temperature,Pressure,Humidity,WindDirection_in_Degrees,Speed,month,day,Hour,Minute,RiseMinute, SetHour,SetMinute]])
    #print(predicted)
    #st.success('solar radiation :',predicted)

if st.button('Check'):
    predicted = Model.predict([[Temperature, Pressure, Humidity, WindDirection_in_Degrees, Speed, month, day, Hour, Minute, RiseMinute, SetHour, SetMinute]])
    #print(predicted)   
    #st.success('solar radiation :',predicted)
    st.success(f'Solar radiation: {predicted[0]}wb')
        