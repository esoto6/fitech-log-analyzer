import streamlit as st
from forms.Upload import upload_form

@st.dialog("Upload File")
def show_upload_form():
    upload_form()

st.title("Fitech Log Visualizer")

# Two-column layout for image and headline
col1, col2 = st.columns([1, 2], gap="small")

with col1:
    st.image("./assets/fitech.jpg", width=750)

with col2:
    st.write("## 🔧 Tune Smarter. Drive Faster")
    st.write(
        "Instantly visualize your FiTech logs, troubleshoot issues, and fine-tune every setting with clarity and confidence."
    )
    st.write(
        "*From logging to precision tuning, this dashboard transforms your data into actionable insights, letting you diagnose, optimize, and dial in your setup like a pro.*"
    )


    st.write("---")


    st.write(
        "### Get Started"
    )
    st.write(
        "Upload your FiTech CSV logs to start analyzing and visualizing your performance data instantly."
    )

    if st.button("Upload File", type="primary"):
        show_upload_form()



if 'uploaded_data' in st.session_state:
    st.write("View Data Here:")
    
    if st.button("Go to Data Grid", type="secondary"):
        st.switch_page("views/Data.py")

    if st.button("Go to Overlay Charts", type="secondary"):
        st.switch_page("views/Overlay.py")

    if st.button("Go to Singular Charts", type="secondary"):
        st.switch_page("views/Singular.py")
