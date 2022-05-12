# Import necessary libraries
import json
import joblib
import datetime

# import pandas as pd
import streamlit as st

# Custom classes 
import os

def app():
    """This application helps in running machine learning models without having to write explicit code 
    by the user. It runs some basic models and let's the user select the X and y variables. 
    """

    # Create dictionary 
    res = {}

    # Use two column technique 
    # col1, col2 = st.columns(2)
    # y_var = col1.radio("Select the variable to be predicted (y)", options=["A", "B"])
    

    # name
    name = st.text_input("Name")

    # start date
    start_date = st.date_input(
     "Start date",
     datetime.date(2019, 7, 6))

     # start date
    end_date = st.date_input(
     "End date",
    datetime.datetime.now())

    # Option to select predition type 
    pred_type = st.radio("Select an option.", 
                        options=["no print", "print"], 
                        help="Write about reg and classification")

    # Add to model parameters 
    res = {
            'X': name,
            'y': start_date, 
            'pred_type': pred_type,
    }

    optionals = st.checkbox('Show optional fields')

    if optionals:

        st.write(f"**Mandatory:** {res}")

        options1 = st.multiselect(
        'What are your favorite colors',
        ['Green', 'Yellow', 'Red', 'Blue'],
        ['Yellow', 'Red'])

        st.write('You selected:', options1)
        
        options2 = st.multiselect(
        'What are your favorite colors2',
        ['A'],
        ['A'])

        st.write('sel 2:', options2)

    