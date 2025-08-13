import streamlit as st
import pandas as df

st.title("Data View Page")

if 'uploaded_data' in st.session_state:
    df = st.session_state['uploaded_data']

    st.write("## Preview of data:")
    st.dataframe(df)

    st.session_state['uploaded_data'] = df