import streamlit as st

# Custom imports 
from multipage import MultiPage
from pages import single_dataset # import your pages here

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.title("Metadata creator for geospatial data")

# Add all your applications (pages) here
app.add_page("Single dataset", single_dataset.app)

# The main app
app.run()