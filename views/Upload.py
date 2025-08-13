import streamlit as st
from Services.FitechFileReader import get_reader


st.title("Upload CSV")

uploaded_file = st.file_uploader("Upload your FiTech CSV file", type=["csv"])

if uploaded_file:
    st.write(f"## Loaded File: {uploaded_file.name}")
    reader = get_reader(uploaded_file.name)
    df = reader.read()

    st.write("## Data Reader:")
    st.write(reader.__class__)

    st.session_state['reader'] = reader.__class__
    st.session_state['uploaded_data'] = df

    st.toast("File uploaded")

if 'uploaded_data' in st.session_state:

    reader = st.session_state['reader']

    st.write("## Data REader")
    st.write(reader)

    with st.container():
        st.write("# View Data Visualization")

        col1, col2, col3 = st.columns(
            3, gap="medium", vertical_alignment="center")

        with col1:
            if st.button("Go to Data Grid", "secondary", type="primary"):
                st.switch_page("views/Data.py")
        with col2:
            if st.button("Go to Overlay Charts", type="primary"):
                st.switch_page("views/Overlay.py")
        with col3:
            if st.button("Go to Singular Charts", type="primary"):
                st.switch_page("views/Singular.py")
