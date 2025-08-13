import streamlit as st


st.set_page_config(
    page_title="Fitech Log Data Visualizer",
    page_icon="",
)

upload_page = st.Page(
    page="views/Upload.py",
    title="Upload CSV",
    icon=":material/upload_file:",
)

data_page = st.Page(
    page="views/Data.py",
    title="Data Grid",
    icon=":material/data_table:",
)

overlay_page = st.Page(
    page="views/Overlay.py",
    title="Overlay Charts",
    icon=":material/analytics:",
)

singular_page = st.Page(
    page="views/Singular.py",
    title="Singular Charts",
    icon=":material/multiline_chart:",
)

terminology = st.Page(
    page="views/Terminology.py",
    title="Terminology",
    icon=":material/contract:",
)

pg = st.navigation(
    {
        "Files": [upload_page],
        "Data Visualization": [data_page, overlay_page, singular_page],
        "FAQ": [terminology]
    }

)

# st.logo("assets/data-logo-2.png")
st.sidebar.text("Edwin Soto")


pg.run()
