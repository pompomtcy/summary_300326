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

# ตรวจสอบ session_state
if "problems" not in st.session_state:
    st.session_state.problems = []

# ฟังก์ชันเพิ่ม problem ใหม่
def add_problem():
    st.session_state.problems.append({"title": "", "detail": "", "management": ""})

# ปุ่มเพิ่ม problem
st.button("Add Problem", on_click=add_problem)

# แสดงปัญหา
for i, problem in enumerate(st.session_state.problems):
    with st.expander(f"Problem {i+1}", expanded=True):
        problem["title"] = st.text_input("Title", value=problem["title"], key=f"title_{i}")
        problem["detail"] = st.text_area("Detail", value=problem["detail"], key=f"detail_{i}")
        problem["management"] = st.text_area("Management", value=problem["management"], key=f"management_{i}")

# สรุปข้อมูล
if st.session_state.problems:
    st.subheader("Summary of Problems")
    for i, problem in enumerate(st.session_state.problems):
        st.markdown(f"**Problem {i+1}: {problem['title']}**")
        st.markdown(f"- Detail: {problem['detail']}")
        st.markdown(f"- Management: {problem['management']}")
