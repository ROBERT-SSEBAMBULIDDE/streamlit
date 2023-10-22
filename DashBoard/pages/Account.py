# create signup and login page with streamlit application user to access the dashboard.
# Feature of the application is to display the user details,secure login, and logout,session management,password reset,
# authentication, and,mongodb user database connection more.User signup store in database

import hashlib

import streamlit as st
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb+srv://cluster1.bak1r58.mongodb.net/')
db = client['user_database']
collection = db['users']

# Session Management (not production-ready)
st.set_page_config(
    page_title="User Authentication System",
    page_icon=":lock:",
    layout="centered"
)


# Security: Password Hashing
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Signup Page
def signup():
    st.title("Signup")
    username = st.text_input("Username", key="signup-username")
    password = st.text_input("Password", type="password", key="signup-password")
    email = st.text_input("Email", key="signup-email")
    if st.button("Signup"):
        # Security: Hash the password before storing it
        hashed_password = hash_password(password)

        # Store user details in the database
        user = {
            "username": username,
            "password": hashed_password,
            "email": email,
            "is_active": True  # User is active by default
        }
        collection.insert_one(user)
        st.success("Signup successful!")


# Login Page
def login():
    st.title("Login")
    username = st.text_input("Username", key="login-username")
    password = st.text_input("Password", type="password", key="login-password")
    if st.button("Login"):
        # Security: Hash the input password to compare with the hashed password in the database
        hashed_password = hash_password(password)

        # Check if the user exists in the database and is active
        user = collection.find_one({"username": username, "password": hashed_password, "is_active": True})
        if user:
            # Session Management: Store user information in a session variable
            st.session_state.user = user

            st.success("Login successful!")

            # Redirect to the user dashboard
            user_dashboard()
        else:
            st.warning("Incorrect username or password")


# User Dashboard
def user_dashboard():
    st.title("User Dashboard")
    st.write(f"Welcome, {st.session_state.user['username']}!")

    # Implement user-specific functionalities here


# Admin Interface (needs authentication and authorization)
def admin_interface():
    st.title("Admin Interface")

    # Implement admin functionalities like creating and deleting users


# Main Application
def main():
    st.title("User Authentication System")

    if "user" in st.session_state:
        user_dashboard()
    else:
        option = st.selectbox("Select an option:", ["Login", "Signup"])

        if option == "Login":
            login()
        else:
            signup()


if __name__ == '__main__':
    main()
