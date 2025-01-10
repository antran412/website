# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 17:45:14 2024

@author: hantr
"""

import streamlit as st
import pickle
import numpy as np
import pandas as pd

def load_model():
    with open('predict.pkl','rb') as file:
              data = pickle.load(file)
    return data

data = load_model()
pred_model = data['model']
sd = data['SD']

def show_predict_page():
    st.title("Biosafety Professionals Salary Prediction")
    
    st.write("""Please fill out the questions below to predict the salary""")
    

    institution_cat = ('Government', 'Academic (Public)', 'Academic (Private)', 'Other')
    
    biosafety_time = ('1-25%','26-50%', '51-75%', '76-100%' )
    
    biosafety_team = ('1','2', '3', '4', '5 or more')
    
    employee_report = ('0', '1', '2', '3', '4 or more',)
    
    data_entry = ('1-25%', '26-50%', '76-100%', '51-75%')
    
    gender= ('Female', 'Male')
    
    age = ('20-29','30-39','40-49','50-59','60-69',  '70 or more', )
    
    education = ('High school graduate or equivalent',"Bachelor's degree or equivalent", 'Master’s degree or equivalent',
           'Doctorate')
    
    experience = ('Less than 1 year', 'At least 1 year but less than 5 years',
            'At least 5 years but less than 10 years',
           'At least 10 years but less than 15 years', 'More than 15 years','Other')
    
    cat_code = {'Government': 1, 'Academic (Public)': 2,'Academic (Private)': 3,'Other': 4}
    time_code = {'1-25%': 1, '26-50%': 2, '51-75%': 3,  '76-100%': 4}
    team_code = {'1': 1, '2': 2, '3': 3,  '4': 4,'5 or more':5}
    emp_code = {'0': 1, '1': 2, '2': 3, '3': 4,'4 or more':5}
    entry_code = {'1-25%': 1, '26-50%': 2,'51-75%': 3,'76-100%': 4}
    gender_code = {'Female':1, 'Male':2}              
    age_code = {'20-29':1, '30-39':2, '40-49':3, '50-59':4, '60-69':5, '70 or more':6 }
    edu_code = {'High school graduate or equivalent':1, "Bachelor's degree or equivalent":2, 
            'Master’s degree or equivalent':3, 
             'Doctorate':4}
    exp_code = {'Less than 1 year':1, 'At least 1 year but less than 5 years':2, 
            'At least 5 years but less than 10 years':3, 
             'At least 10 years but less than 15 years':4, 
            'More than 15 years':5, 'Other':6}
    
    institution = st.selectbox("Institution Category", institution_cat)
    
    time = st.selectbox("How many percentage of time do you spend on biosafety responsibility?", biosafety_time)
    
    team = st.selectbox("How many professionals are there in your biosafety team?", biosafety_team)
    
    report = st.selectbox("How many employees are there to report to you?", employee_report)

    entry = st.selectbox("How many percentage of time do you spend on data entry and record-keeping tasks?", data_entry)
    
    gender = st.selectbox('What is your gender?', gender)
    
    age = st.selectbox('What is your age range?', age)
    
    education = st.selectbox('What is your hghest education level?', education)
    
    experience = st.selectbox('What is your working experience in the field?', experience)
    
    ok = st.button("Predict Salary")
    
    if ok: 
        x = np.array([[institution, time, team, report, entry, gender, age, education, experience]])
        x[:, 0]= pd.Series(x[:, 0]).map(cat_code).values
        x[:, 1]= pd.Series(x[:, 1]).map(time_code).values
        x[:, 2]= pd.Series(x[:, 2]).map(team_code).values
        x[:, 3]= pd.Series(x[:, 3]).map(emp_code).values
        x[:, 4]= pd.Series(x[:, 4]).map(entry_code).values
        x[:, 5]= pd.Series(x[:, 5]).map(gender_code).values
        x[:, 6]= pd.Series(x[:, 6]).map(age_code).values
        x[:, 7]= pd.Series(x[:, 7]).map(edu_code).values
        x[:, 8]= pd.Series(x[:, 8]).map(exp_code).values
        x = x.astype(int)
        
        salary = pred_model.predict(x)
        lower = salary - sd
        upper = salary + sd
        st.subheader(f"The estimated salary is ${salary[0]:,.2f}")
        st.write(f"The standard deviation is ${sd:,.2f}")


