import streamlit as st


st.set_page_config(
    page_title="Fitech Log Data Visualizer",
    page_icon="",
    layout="wide"
)

home_page = st.Page(
    page="views/Home.py",
    title="Home",
    icon=":material/home:",
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
        "Home":[home_page],
        "Data Visualization": [data_page, overlay_page, singular_page],
        "FAQ": [terminology]
    }

)

# st.logo("assets/data-logo-2.png")
st.sidebar.text("Edwin Soto")


pg.run()
