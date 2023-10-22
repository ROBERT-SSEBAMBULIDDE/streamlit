# DESIGN HOME PAGE OF DATA ANALYTICS DASHBOARD
# import libraries
import streamlit as st

# creating Page setup size
st.set_page_config(layout="wide")

# create horizontal navigation menu of pages


# Header of the page
# Logo: Place your company or dashboard logo at the top-left corner for brand recognition.
# DisplayLogo: Place your company or dashboard logo at the top-left corner  for brand recognition.
header_html = """
    <div style="display: flex; align-items: center;">
        <img src="https://www.pridemicrofinance.co.ug/img/saving-imgs/pride-logo-official.png" style="width: 100px; height: 100px; margin-right: 10px;">
        <h1 style="font-size: 36px; margin: 0;color: green;">Pride Microfinance Ltd</h1>
    </div>
"""
st.markdown(header_html, unsafe_allow_html=True)

# set slogan with light blue color bold text
st.write('<p style="color:lightblue; font-weight:bold;">Your Growth Is Our Pride</p>', unsafe_allow_html=True)

# run the application
