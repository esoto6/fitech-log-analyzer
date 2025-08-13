import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from FitechFileReader import get_reader

st.title("FiTech Log Data Visualizer")

uploaded_file = st.file_uploader("Upload your FiTech CSV file", type=["csv"])
print(uploaded_file)


if uploaded_file:
    st.write(f"# File: {uploaded_file.name}")
    reader = get_reader(uploaded_file.name)
    df = reader.read()

    tabData, tabOverlay, tabSeperate = st.tabs(["Raw Data", "Overlay Plot", "Seperate Plot"], width="stretch")

    with tabData:
        st.write("# Data Reader:")
        st.write(reader.__class__)
        st.write("### Preview of data:")
        st.dataframe(df.head(20))

    with tabOverlay:
        numeric_cols_Overlay = df.select_dtypes(include=['number']).columns.tolist()
        selected_cols_Overlay = st.multiselect("Select fields to plot vs Time", options=numeric_cols_Overlay, default=['RPM', 'Fuel PW', 'MAP', 'AFR'], key="overlay")

        fig, ax = plt.subplots(figsize=(12, 6))
        for col in selected_cols_Overlay:
            ax.plot(df['Time'], df[col], label=col)
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Value")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)

   
    with tabSeperate:
        numeric_cols_Seperate= df.select_dtypes(include=['number']).columns.tolist()
        selected_cols_Seperate = st.multiselect("Select fields to plot vs Time", options=numeric_cols_Seperate, default=['RPM', 'Fuel PW', 'TPS', 'AFR'], key="seperate")

        fig, axs = plt.subplots(len(selected_cols_Seperate), 1, figsize=(12, 4 * len(selected_cols_Seperate)), sharex=True)
        if len(selected_cols_Seperate) == 1:
            axs = [axs]
        for ax, col in zip(axs, selected_cols_Seperate):
            ax.plot(df['Time'], df[col], label=col)
            ax.set_ylabel(col)
            ax.grid(True)
            ax.legend()
        axs[-1].set_xlabel("Time (s)")
        plt.tight_layout()
        st.pyplot(fig)