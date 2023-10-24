# header with left aligned symbol  to represent credit department of a bank and unique slogan in relation to credit
# as an inline header with the symbol with green color and background header of money image.Use streamlit and other
# libraries

import streamlit as st

# Create a continuously moving announcement bar
announcement = "Demo Announcement: We are offering special credit rates this month! Contact us for details. " * 10  # Repeat for continuous scrolling
st.markdown(
	f"""
    <style>
    .announcement {{
        background-color: green;
        color: white;
        text-align: center;
        padding: 10px;
        font-weight: bold;
        overflow: hidden;
        white-space: nowrap;
        animation: marquee 20s linear infinite;
    }}

    @keyframes marquee {{
        0% {{ transform: translateX(100%); }}
        100% {{ transform: translateX(-100%); }}
    }}
    </style>
    <div class="announcement">{announcement}</div>
    """,
	unsafe_allow_html=True
)

# Create the header with colored text
header_html = f"""
<div style="display: flex; align-items: center; padding: 20px; background-color: green; color: white;">
    <div style="font-size: 36px; margin-right: 20px; font-weight: bold;">Credit Department</div>
    <div>
        <h2 style="font-weight: bold; color: lightblue;">Your Trusted Partner in Credit Solutions</h2>
    </div>
</div>
"""

st.markdown(header_html, unsafe_allow_html=True)

# The rest of your Streamlit app content goes here
