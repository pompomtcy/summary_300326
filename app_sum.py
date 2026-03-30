import streamlit as st
st.title("My Discharge Summary 🚀")
name = st.text_input("Patient's name")
age = st.text_input("Age")

gender = st.radio("Gender", ["Male", "Female"], horizontal=True)
underlying = st.text_input("U/D")
history = st.text_input("Present illness")
admit_date = st.date_input("Admit date", value=None)
discharge_date = st.date_input("Discharge date", value=None)

st.subheader("Problem List Form")

# เตรียม session state เก็บปัญหา
if "problems" not in st.session_state:
    st.session_state.problems = []

# ฟังก์ชันเพิ่ม problem ใหม่
def add_problem():
    st.session_state.problems.append({"problem": "", "detail": "", "management": ""})

# ปุ่มเพิ่ม problem
st.button("Add Problem", on_click=add_problem)

# แสดงปัญหาที่มี
for i, problem in enumerate(st.session_state.problems):
    with st.expander(f"Problem {i+1}"):
        problem["problem"] = st.text_input(f"Problem {i+1}", value=problem["problem"], key=f"problem_{i}")
        problem["detail"] = st.text_area(f"Detail {i+1}", value=problem["detail"], key=f"detail_{i}")
        problem["management"] = st.text_area(f"Management {i+1}", value=problem["management"], key=f"management_{i}")
