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

st.title("Problem List Form")

# ตรวจสอบ session_state และเริ่มต้นด้วย Problem 1
if "problems" not in st.session_state:
    st.session_state.problems = [{"title": "", "detail": "", "management": ""}]

# ฟังก์ชันเพิ่ม problem ใหม่
def add_problem():
    st.session_state.problems.append({"title": "", "detail": "", "management": ""})

# ปุ่มเพิ่ม problem
st.button("Add Problem", on_click=add_problem)

# แสดงปัญหาทั้งหมด
for i, problem in enumerate(st.session_state.problems):
    with st.expander(f"Problem {i+1}", expanded=True):
        problem["title"] = st.text_input("Title", value=problem["title"], key=f"title_{i}")
        problem["detail"] = st.text_area("Detail", value=problem["detail"], key=f"detail_{i}")
        problem["management"] = st.text_area("Management", value=problem["management"], key=f"management_{i}")



