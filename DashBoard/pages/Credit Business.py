# header with left aligned symbol  to represent credit department
# of a bank and unique slogan in relation to credit
# as an inline header with the symbol with green color and
# background header of money image.Use streamlit and other
# libraries

import streamlit as st
import pandas as pd
import pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Set the page configuration for a wider layout
st.set_page_config(layout="wide")   

# Create a continuously moving announcement bar with green and light blue text
announcement = "Announcement: We are offering special credit rates this month! Contact us for details."
st.markdown(
    f"""
    <style>
    .announcement {{
        background-color: none;
        color: green;
        text-align: center;
        padding: 20px;
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

# Create a left-aligned header in green color, bold font size 30px, and left-aligned h1 heading
st.markdown("<h1 style='font-size: 40px; color: green; font-weight: bold; text-align: left;'>Credit Business Analytics</h1>", unsafe_allow_html=True)
# Create a left-aligned header in light blue color, bold font size 24px, and left-aligned h2 heading
st.markdown("<h2 style='font-size: 24px; color: lightblue; font-weight: bold; text-align: left;'>Credit Business Insights</h2>", unsafe_allow_html=True)

# Load environment variables from .env file and connect to MongoDB
#define the connection variables
url = os.getenv('url')
database = os.getenv('database_name')
collection= os.getenv('collection_name')


load_dotenv()
#connect to mongodb
client = MongoClient(os.getenv('url'))
# select database
db = client["database"]
# select collection
collection = db["collection"] 

# high level filter of data
df = pd.DataFrame(list(collection.find()))

# Perform data preprocessing operations on the dataframe
# Set desired dataframe options
pd.set_option("display.max_columns", None)  # Show all columns
pd.set_option("display.max_rows", None)  # Show all rows
pd.set_option("display.width", None)  # Set display width to fit all columns
pd.set_option("display.precision", 2)  # Set decimal precision to 2

# preprocessing of data
# show data columns
df_columns = df.columns
print(df_columns)

# Shape
print(df.shape)
# find missing values
missing_values = df.isnull().sum()
print(missing_values)

# deleting last 2 rows
df = df.drop(df.index[-2:])
# deleting some columns
columns_to_delete = ['_id']
df = df.drop(columns=columns_to_delete)

# reindex the dataframe with a SN Column
df = df.set_index("S/N")
# fit the columns in the dataframe
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# updating database column names with new names
# renaming columns and creating new columns
df = df.rename(columns={'disbursed_by': 'Credit Officer',
                        'disbursed_\n\namount': 'Amount Disbursed',
                        'group_\n\ncustomer_number': 'Group Number'})

# list of branch_names from the data
# = df['branch_names'].unique().tolist()
#print(branch_names)

# show data types
print(df.dtypes)

# print dataframe first 5 rows
print(df.head(20))
# tail
# print(df.tail(10))
