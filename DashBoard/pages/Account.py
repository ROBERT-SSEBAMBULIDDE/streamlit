# Login/Sign-up:Use Streamlit to create a login and sign-up form.You can use MongoDB to store user credentials.
# Recommended packages: Streamlit, pymongo, bcrypt,authentication,hashlib and others
# option button for login and signup show up at the bottom of the page
# include option and button for user to reset password using registered email address,
# enter a valid email address and confirm password
import streamlit as st
import pymongo
import bcrypt

# Title and page configuration
st.title("User Login and Sign-up")

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://username:password@localhost:27017/")
db = client["your_database_name"]
collection = db["users"]

# Functions for user registration and login
def register_user(username, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    collection.insert_one({"username": username, "password": hashed_password})

def login_user(username, password):
    user = collection.find_one({"username": username})
    if user and bcrypt.checkpw(password.encode('utf-8'), user["password"]):
        return True
    return False

page = st.sidebar.selectbox("Choose a page", ["Login", "Sign-up"])

if page == "Sign-up":
    st.subheader("Sign Up")
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Register"):
        if new_password == confirm_password:
            existing_user = collection.find_one({"username": new_username})
            if existing_user is None:
                register_user(new_username, new_password)
                st.success("Registration successful!")
            else:
                st.error("Username already exists. Please choose a different one.")
        else:
            st.error("Passwords do not match.")

if page == "Login":
    st.subheader("Log In")
    login_username = st.text_input("Username")
    login_password = st.text_input("Password", type="password")

    if st.button("Login"):
        if login_user(login_username, login_password):
            st.success("Logged in as " + login_username)
        else:
            st.error("Login failed. Check your credentials.")
            
            #robert
            



