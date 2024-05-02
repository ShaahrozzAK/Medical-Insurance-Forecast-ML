
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

model = pickle.load(open("model.pkl", "rb"))

st.set_page_config(page_title="Medical Issurance Forcast Application")
# page title
st.title('Medical Issurance Forcast using ML Model')
    
    
# getting the input data from the user
col1, col2, col3 = st.columns(3)
    
with col1:
    age = st.text_input('Age of Person')
        
with col2:
    sex = st.text_input('Gender of Person')
    if sex=="male":
        sex_female= False
        sex_male= True
    if sex=="female":
        sex_female= True
        sex_male= False
    
with col3:
    bmi = st.text_input('Body Mass Index (BMI)')
    
with col1:
    children = st.text_input('No. of children')
    
with col2:
    smoker = st.text_input('Does the Person Smoke?')
    if smoker=="yes":
        smoker_no= False
        smoker_yes= True
    if smoker=="no":
        smoker_no= True
        smoker_yes= False
with col3:
    region = st.text_input('Residence Region')
    if region=="southeast":
        region_southeast= True
        region_southwest= False
        region_northeast= False
        region_northwest= False
    if region=="southwest":
        region_southeast= False
        region_southwest= True
        region_northeast= False
        region_northwest= False
    if region=="northeast":
        region_southeast= False
        region_southwest= False
        region_northeast= True
        region_northwest= False
    if region=="northwest":
        region_southeast= False
        region_southwest= False
        region_northeast= False
        region_northwest= True
    
# creating a button for Prediction
if st.button('Generate Result'):
    prediction = model.predict([[int(age), float(bmi), int(children), sex_female, sex_male, smoker_no, smoker_yes, region_northeast, region_northwest, region_southeast, region_southwest]])
    st.success("The Predicted Medical Issurance Forcast Amount: "+ str(prediction[0,0]))
