import streamlit as st
import pymongo
import pandas as pd

# Connect to the MongoDB database
client = pymongo.MongoClient("mongodb+srv://rssebambulidde:19Sseba15@cluster1.bak1r58.mongodb.net/")
db = client["Pride_Microfinance"]

# Set the page configuration for a wider layout
st.set_page_config(page_title="MongoDB Data Uploader", layout="wide")

# Step 1: Choose Collection
st.header("Step 1: Choose a Collection")
st.write("Select the collection in your MongoDB database where you want to upload data.")

# Define available collection options
collection_options = ["Disbursements", "WrittenOffLoans"]
selected_collection = st.selectbox("Choose a collection", collection_options)

# Get the selected collection
collection = db[selected_collection]

# Step 2: File Upload
st.header("Step 2: Upload a CSV File")
st.write("You can upload a CSV file from your local machine.")

# Create a file uploader widget with a file type restriction
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    # Read the uploaded file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Step 3: Submit Data
    st.header("Step 3: Submit Data")
    st.write("Click the 'Submit' button to upload your data to the selected collection.")

    # Create a submit button to upload data
    if st.button("Submit"):
        # Insert the data into the collection
        collection.insert_many(df.to_dict("records"))

        # Verification message
        st.success(f"Data uploaded to '{selected_collection}' collection.")

        # Additional Notes
        st.header("Additional Notes:")
        st.write("- The data has been successfully uploaded.")
        st.write("- If you need to upload more data or have other tasks, you can continue using the application.")
















