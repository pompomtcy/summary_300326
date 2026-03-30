import streamlit as st
st.title("My Discharge Summary 🚀")
name = st.text_input("Patient's name")
age = st.text_input("Age")

gender = st.radio("Gender", ["Male", "Female"], horizontal=True)
