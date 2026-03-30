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

st.title("Problem List Form (Multiple Follow-up Choices)")

# เริ่มต้นด้วย Problem 1
if "problems" not in st.session_state:
    st.session_state.problems = [{
        "title": "", 
        "detail": "", 
        "management": "", 
        "followup_choices": [],
        "dc_fu_detail": "",
        "refer_opd_detail": "",
        "refer_ipd_hospital": "",
        "dc_against_detail": ""
    }]

# ฟังก์ชันเพิ่ม Problem
def add_problem():
    st.session_state.problems.append({
        "title": "", 
        "detail": "", 
        "management": "", 
        "followup_choices": [],
        "dc_fu_detail": "",
        "refer_opd_detail": "",
        "refer_ipd_hospital": "",
        "dc_against_detail": ""
    })

st.button("Add Problem", on_click=add_problem)

# แสดง Problem ทั้งหมด
for i, problem in enumerate(st.session_state.problems):
    with st.expander(f"Problem {i+1}", expanded=True):
        problem["title"] = st.text_input("Title", value=problem["title"], key=f"title_{i}")
        problem["detail"] = st.text_area("Detail", value=problem["detail"], key=f"detail_{i}")
        problem["management"] = st.text_area("Management", value=problem["management"], key=f"management_{i}")
        
        # เลือกหลายช้อยได้
        followup_options = [
            "D/C no F/U",
            "D/C + F/U",
            "Refer OPD case",
            "Refer IPD case",
            "D/C against advise",
            "Death"
        ]
        problem["followup_choices"] = st.multiselect(
            "Select Follow-up/Disposition Options",
            followup_options,
            default=problem["followup_choices"],
            key=f"followup_{i}"
        )
        
        # Dynamic fields ตามช้อย
        if "D/C + F/U" in problem["followup_choices"]:
            problem["dc_fu_detail"] = st.text_area(
                "D/C + F/U Details",
                value=problem["dc_fu_detail"],
                key=f"dc_fu_{i}"
            )
        else:
            problem["dc_fu_detail"] = ""
        
        if "Refer OPD case" in problem["followup_choices"]:
            problem["refer_opd_detail"] = st.text_area(
                "Refer OPD Details",
                value=problem["refer_opd_detail"],
                key=f"refer_opd_{i}"
            )
        else:
            problem["refer_opd_detail"] = ""
        
        if "Refer IPD case" in problem["followup_choices"]:
            problem["refer_ipd_hospital"] = st.text_input(
                "Refer IPD Hospital Name",
                value=problem["refer_ipd_hospital"],
                key=f"refer_ipd_{i}"
            )
        else:
            problem["refer_ipd_hospital"] = ""
        
        if "D/C against advise" in problem["followup_choices"]:
            problem["dc_against_detail"] = st.text_area(
                "D/C against advise Details",
                value=problem["dc_against_detail"],
                key=f"dc_against_{i}"
            )
        else:
            problem["dc_against_detail"] = ""

# สรุปข้อมูล
if st.session_state.problems:
    st.subheader("Summary of Problems")
    for i, problem in enumerate(st.session_state.problems):
        st.markdown(f"**Problem {i+1}: {problem['title']}**")
        st.markdown(f"- Detail: {problem['detail']}")
        st.markdown(f"- Management: {problem['management']}")
        st.markdown(f"- Follow-up Choices: {', '.join(problem['followup_choices']) if problem['followup_choices'] else 'None'}")
        if problem["dc_fu_detail"]:
            st.markdown(f"  - D/C + F/U Details: {problem['dc_fu_detail']}")
        if problem["refer_opd_detail"]:
            st.markdown(f"  - Refer OPD Details: {problem['refer_opd_detail']}")
        if problem["refer_ipd_hospital"]:
            st.markdown(f"  - Refer IPD Hospital: {problem['refer_ipd_hospital']}")
        if problem["dc_against_detail"]:
            st.markdown(f"  - D/C against advise Details: {problem['dc_against_detail']}")



