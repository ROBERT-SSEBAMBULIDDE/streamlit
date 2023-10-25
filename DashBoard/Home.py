# DESIGN HOME PAGE OF DATA ANALYTICS DASHBOARD
# save the codes in blocks
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

# set up the page tittle that is green bold text,centered,h1 heading,font size 36px
title_html = """
    <h1 style="font-size: 36px; text-align: center; color: green; font-weight: bold;">Pride Data Analytics</h1>
"""
st.markdown(title_html, unsafe_allow_html=True)

# description of the web application with its purpose when it is h2 heading center justified,font size 24px
description_html = """
    <h2 style="font-size: 18px; text-align: center;">This web application provides data analytics 
    for Pride Microfinance Ltd. It allows users to analyze and visualize various
     financial and risk-related data to make informed decisions and drive business growth.</h2>
"""
st.markdown(description_html, unsafe_allow_html=True)

# Sub tittle or heading of the page with light blue color bold text
sub_title_html = """
<h2 style="font-size: 24px; text-align: center; color: lightblue; 
font-weight: bold;">Pride Data Analytics Categories</h2>
"""
st.markdown(sub_title_html, unsafe_allow_html=True)

# Categories of the analytics the application provides
# create row for each category tittle and markdown the description of the category under it which is hidden but
# visible on hover.make the tittles of the categories bold,green color,font size 24px and description boxed frame
category_html = """
<div style="border: 15px solid lightgray; padding: 15px; margin-bottom: 15px; cursor: pointer;">
    <h2 style="font-size: 24px; color: green; font-weight: bold;">{category_title}</h2>
    <div style="display: none;">
        <p>{category_description}</p>
    </div>
</div>
"""

categories = [
	{"title": "Descriptive Analytics",
	 "description": "This form of analytics involves summarizing historical data to understand what has happened in the past. It includes techniques like data visualization, reporting, and dashboards. Descriptive analytics provides a snapshot of the current state of affairs."},
	{"title": "Diagnostic Analytics",
	 "description": "Diagnostic analytics focuses on determining why a certain event or trend occurred. It involves investigating historical data to identify the root causes of specific outcomes or issues."},
	{"title": "Predictive Analytics",
	 "description": "Predictive analytics uses historical data and statistical algorithms to make predictions about future events or trends. It is often used for forecasting, risk assessment, and recommendation systems."},
	{"title": "Prescriptive Analytics",
	 "description": "Prescriptive analytics takes predictive analytics a step further by suggesting actions to take in response to predicted outcomes. It helps decision-makers optimize their choices by providing recommendations for the best course of action."},
	{"title": "Exploratory Data Analysis (EDA)",
	 "description": "EDA is an initial analysis of data to discover patterns, relationships, or anomalies. It often involves data visualization and statistical methods to uncover insights and hypotheses for further investigation."},
	{"title": "Text Analytics",
	 "description": "Text analytics focuses on analyzing unstructured textual data, such as customer reviews, social media posts, and documents, to extract valuable information and sentiment analysis."},
	{"title": "Sentiment Analysis",
	 "description": "This is a subset of text analytics that assesses the sentiment or emotional tone expressed in text, helping businesses understand customer opinions and feelings."},
	{"title": "Time Series Analysis",
	 "description": "Time series analytics deals with data points collected or recorded over time. It is particularly useful for forecasting future values, identifying trends, and understanding seasonality."},
	{"title": "Spatial Analytics",
	 "description": "Spatial analytics involves analyzing geographic data to extract insights. It is commonly used in applications like geospatial mapping, location-based services, and resource allocation."},
	{"title": "Web Analytics",
	 "description": "Web analytics focuses on understanding website or online platform usage. It helps businesses track user behavior, conversion rates, and other online metrics."},
	{"title": "Social Media Analytics",
	 "description": "Social media analytics involves analyzing data from social media platforms to gain insights into audience behavior, sentiment, and trends."},
	{"title": "Big Data Analytics",
	 "description": "Big data analytics deals with massive volumes of data, often using distributed computing and advanced algorithms to process and analyze the data efficiently. It includes tools like Hadoop and Spark."},
	{"title": "Business Intelligence (BI)",
	 "description": "BI analytics involves using data to support business decision-making. It includes the use of reporting tools, dashboards, and key performance indicators (KPIs) to monitor business performance."},
	{"title": "Machine Learning and Artificial Intelligence",
	 "description": "Machine learning and AI techniques are used to develop models that can analyze data and make predictions or classifications. This includes techniques like clustering, classification, regression, and deep learning."}
]
# loop through the categories and create a row for each category
for category in categories:
	category_title = category["title"]
	category_description = category["description"]

	category_html = """
    <div style="border: 15px solid lightgray; padding: 15px; margin-bottom: 15px; cursor: pointer;">
        <h2 style="font-size: 24px; color: green; font-weight: bold;">{}</h2>
        <div style="display: none;">
            <p>{}</p>
        </div>
    </div>
    """.format(category_title, category_description)

	# Display the category row
	st.markdown(category_html, unsafe_allow_html=True)
	# Display the category description
	st.markdown(category_description, unsafe_allow_html=True)
