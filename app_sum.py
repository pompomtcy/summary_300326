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

# --- Follow-up / Disposition ---
cases = []

if st.checkbox("D/C no F/U"):
    cases.append("D/C no F/U")

if st.checkbox("D/C + F/U"):
    extra = st.text_input("OPD:")
    cases.append(f"D/C + F/U {extra}" if extra else "D/C + F/U")

if st.checkbox("Refer OPD case"):
    extra = st.text_input("FOR:")
    cases.append(f"Refer OPD case {extra}" if extra else "Refer OPD case")

if st.checkbox("Refer IPD case"):
    hospital = st.text_input("Hospital:")
    for_whom = st.text_input("FOR:")
    text = "Refer IPD "
    if hospital:
        text += f" - โรงพยาบาล {hospital}"
    if for_whom:
        text += f" - for {for_whom}"
    cases.append(text)

if st.checkbox("D/C against advise"):
    extra = st.text_input("due to:")
    cases.append(f"D/C against advise due to {extra}" if extra else "D/C against advise")

if st.checkbox("Death"):
    cases.append("Death")

note = st.text_input("Note")

# --- ปุ่มแสดงผล ---
if st.button("Report"):
    output = f"{name}\nผู้ป่วย {gender}   อายุ {age} ปี\nU/D: {underlying}\n\n"
    output += f"Admit วันที่ {admit_date} ถึง {discharge_date}\n\n"
    output += "Problem list:\n"
    for i, problem in enumerate(st.session_state.problems, 1):
        output += f"{i}. {problem['title']}\n"
        output += f"   {problem['detail']}\n"
        output += f"   Mx: {problem['management']}\n\n"
    
    if cases:
        for item in cases:
            output += f"- {item}\n\n"
    output += f"{note}"
    st.text_area("Discharge Summary", output, height=600)

#download
st.download_button(
    label="Download Report as TXT",
    data=output,         
    file_name=f"{name}_dc.txt",
    mime="text/plain"
)

