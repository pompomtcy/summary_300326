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

# --- Follow-up / Disposition สำหรับคนไข้ ---
followup_options = [
    "D/C no F/U",
    "D/C + F/U",
    "Refer OPD case",
    "Refer IPD case",
    "D/C against advise",
    "Death"
]
followup_choices = st.multiselect("Select Follow-up/Disposition Options", followup_options)

# Dynamic fields ตาม Follow-up
dc_fu_detail = ""
refer_opd_detail = ""
refer_ipd_hospital = ""
dc_against_detail = ""

if "D/C + F/U" in followup_choices:
    dc_fu_detail = st.text_area("D/C + F/U Details")
if "Refer OPD case" in followup_choices:
    refer_opd_detail = st.text_area("Refer OPD Details")
if "Refer IPD case" in followup_choices:
    refer_ipd_hospital = st.text_input("Refer IPD Hospital Name")
if "D/C against advise" in followup_choices:
    dc_against_detail = st.text_area("D/C against advise Details")

# --- Problem List ---
if "problems" not in st.session_state:
    st.session_state.problems = [{"title": "", "detail": "", "management": ""}]

def add_problem():
    st.session_state.problems.append({"title": "", "detail": "", "management": ""})

st.button("Add Problem", on_click=add_problem, key="add_problem_button")

for i, problem in enumerate(st.session_state.problems):
    with st.expander(f"Problem {i+1}", expanded=True):
        problem["title"] = st.text_input("Title", value=problem["title"], key=f"title_{i}")
        problem["detail"] = st.text_area("Detail", value=problem["detail"], key=f"detail_{i}")
        problem["management"] = st.text_area("Management", value=problem["management"], key=f"management_{i}")

# --- สรุปข้อมูล ---
st.subheader("Summary")
st.markdown(f"**Patient:** {name}, Age: {age}, Gender: {gender}")
st.markdown(f"**Follow-up Choices:** {', '.join(followup_choices) if followup_choices else 'None'}")
if dc_fu_detail:
    st.markdown(f"- D/C + F/U Details: {dc_fu_detail}")
if refer_opd_detail:
    st.markdown(f"- Refer OPD Details: {refer_opd_detail}")
if refer_ipd_hospital:
    st.markdown(f"- Refer IPD Hospital: {refer_ipd_hospital}")
if dc_against_detail:
    st.markdown(f"- D/C against advise Details: {dc_against_detail}")

if st.session_state.problems:
    st.subheader("Problem List")
    for i, problem in enumerate(st.session_state.problems):
        st.markdown(f"**Problem {i+1}: {problem['title']}**")
        st.markdown(f"- Detail: {problem['detail']}")
        st.markdown(f"- Management: {problem['management']}")
