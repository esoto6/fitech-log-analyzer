import streamlit as st
import pandas as df
import plotly.graph_objects as go

st.title("Overlay Plot Page")


if 'uploaded_data' in st.session_state:
    
    df = st.session_state['uploaded_data']
    numeric_cols_Overlay = df.select_dtypes(include=['number']).columns.tolist()
    selected_cols_Overlay = st.multiselect("Select fields to plot vs Time", options=numeric_cols_Overlay, default=['RPM', 'Fuel PW', 'MAP'], key="overlay")
    
    time_labels = [f"{t:.1f}" for t in df['Time']]

    start_time_str, end_time_str = st.select_slider(
        "Select a range of time (s)",
        options=time_labels,
        value=(time_labels[0], time_labels[-1])
    )

    start_time = float(start_time_str)
    end_time = float(end_time_str)

    filtered_df = df[(df['Time'] >= start_time) & (df['Time'] <= end_time)]

    fig = go.Figure()

    for col in selected_cols_Overlay:
        fig.add_trace(go.Scatter(x=filtered_df['Time'], y=filtered_df[col], mode='lines', name=col, hoverinfo='x+y+name'))

    fig.update_layout(
        title="Interactive Log Viewer",
        xaxis_title="Time (s)",
        yaxis_title="Value",
        legend_title="Legend",
        template="plotly_white",
        hovermode="x unified",
        dragmode="zoom"
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("No Data has been uploaded")
