import streamlit as st
import pandas as pd 
import numpy as  np

import os
import joblib
import hashlib # to hash the password, we can also use passlib or bcrypt libraries as well

import matplotlib.pyplot as plt 
import seaborn as sns
import matplotlib 
matplotlib.use('Agg')

# DB
from managed_db import *

# Password Hashing
def generate_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

# Verify Password
def verify_hashes(password, hashed_text):
    if generate_hashes(password) == hashed_text:
        return hashed_text
    else:
        return False

def main():
    """Mortality Predictioin App"""
    st.title("Disease Mortality Prediction App")

    menu = ['Home', 'Login', 'SignUp']
    submenu = ['Plot', 'Prediction', 'Metrics']

    choice = st.sidebar.selectbox("Menu", menu)
    if choice=="Home":
        st.subheader('Home')
        st.text("What is Hepatitis?")

    elif choice=="Login":
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type='password')
        if st.sidebar.checkbox("Login"):
            create_usertable()
            hashed_password = generate_hashes(password)
            result = login_user(username, verify_hashes(password, hashed_password))
            if result:
                st.success("Welcome {}". format(username))

                activity = st.selectbox("Activity", submenu)
                if activity == "Plot":
                    st.subheader("Data Vis Plot")
                    df = pd.read_csv()
                elif activity == "Prediction":
                    st.subheader("Predictive Analytics")


            else:
                st.warning("Incorrect Username or Password")

    elif choice == "SignUp":
        new_user_name = st.text_input("User name")
        new_password = st.text_input("Password", type='password')
        
        confirm_password = st.text_input("Confirm Password", type='password')
        if (confirm_password == new_password) and (new_password != ""):
            st.success("Password Confirmed")

        if st.button("Submit"):
            if confirm_password != new_password:
                st.warning("Password are not same. Try again")
            else:
                create_usertable()
                hashed_new_password = generate_hashes(new_password)
                add_userdata(new_user_name, hashed_new_password)
                st.success("You have succesfully created a new account")


    


if __name__=="__main__":
    main()

