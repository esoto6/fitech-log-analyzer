import streamlit as st
from Services.FitechFileReader import get_reader


def upload_form():
    with st.form("csv_form"):


        uploaded_file = st.file_uploader("Upload your FiTech CSV file", type=["csv"])
        submit_btn = st.form_submit_button("Submit", type="primary")

        if submit_btn:

            if uploaded_file is not None:
            
                reader = get_reader(uploaded_file.name, uploaded_file)
                df = reader.read()
                st.session_state['reader'] = reader.__class__
                st.session_state['uploaded_data'] = df
                st.success("Form Uploaded Successfull!")
                
            else:
                st.warning("Please select a valid CSV file")

