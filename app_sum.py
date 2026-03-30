import streamlit as st
from datetime import date

st.title("My Discharge Summary 🚀")
name = st.text_input("Patient's name")
age = st.text_input("Age")

gender = st.radio("Gender", ["ชาย", "หญิง"], horizontal=True)
underlying = st.text_input("U/D")
history = st.text_input("Present illness")
admit_date = st.date_input("Admit date", value=None)
discharge_date = st.date_input("Discharge date", value=None)

st.subheader("Problem List Form")

# ตรวจสอบ session_state และเริ่มต้นด้วย Problem 1
if "problems" not in st.session_state:
    st.session_state.problems = [{"title": "", "detail": "", "management": ""}]

# ฟังก์ชันเพิ่ม problem ใหม่
def add_problem():
    st.session_state.problems.append({"title": "", "detail": "", "management": ""})

# แสดงปัญหาทั้งหมด
for i, problem in enumerate(st.session_state.problems):
    with st.expander(f"Problem {i+1}", expanded=True):
        problem["title"] = st.text_input("Title", value=problem["title"], key=f"title_{i}")
        problem["detail"] = st.text_area("Detail", value=problem["detail"], key=f"detail_{i}")
        problem["management"] = st.text_area("Management", value=problem["management"], key=f"management_{i}")

# ปุ่มเพิ่ม problem
st.button("Add Problem", on_click=add_problem)

agree_case1 = st.checkbox("D/C no F/U")
agree_case2 = st.checkbox("D/C + F/U")
if agree_case2:
    extra_text2 = st.text_input("OPD:")
agree_case3 = st.checkbox("Refer OPD case")   
if agree_case3:
    extra_text3 = st.text_input("FOR:") 
agree_case4 = st.checkbox("Refer IPD case")  
if agree_case4:
    extra_text41 = st.text_input("hospital:")
    extra_text42 = st.text_input("for:")
agree_case5 = st.checkbox("D/C against advise") 
if agree_case5:
    extra_text5 = st.text_input("due to:")
agree_case6 = st.checkbox("Death") 

# --- ปุ่มแสดงผล ---
if st.button("Report"):
    output = f"{name}\nผู้ป่วย{gender}   อายุ {age} ปี\nU/D: {underlying}\n\n"
    output += f"Admit วันที่: {admit_date} ถึง {discharge_date}\n\n"
    output += "Problem list:\n"
    for i, problem in enumerate(st.session_state.problems, 1):
        output += f"{i}.{problem['title']}\n"
        output += f"{ problem['detail']}\n"
        output += f" Mx: {problem['management']}\n\n"
    if agree_case1: 
    output = "D/C no F/U"
    st.text_area("Discharge Summary Preview", output, height=400)

