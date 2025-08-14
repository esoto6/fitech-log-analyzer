import streamlit as st
import pandas as pd
from streamlit_slickgrid import slickgrid

st.title("Data View Page")

if 'uploaded_data' in st.session_state:
    df = st.session_state['uploaded_data']

    st.write("## Preview of data:")
    st.dataframe(df)

    grid_options = {
        "enableSorting": True,
        "enableFilter": True,
        "editable": True,
        "autoHeight": True,
        "minHeight": 400
    }
    
    data = df.fillna(0).to_dict(orient='records')
    columns = df.columns
    out = slickgrid(data=data, columns=columns, options=grid_options, key="data_grid" )
else:
    st.warning("No Data has been uploaded")