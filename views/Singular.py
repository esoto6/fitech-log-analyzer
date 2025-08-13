import streamlit as st
import pandas as df
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.title("Singular Plot Page")

if 'uploaded_data' in st.session_state:
    df = st.session_state['uploaded_data']
    numeric_cols_Seperate= df.select_dtypes(include=['number']).columns.tolist()
    selected_cols_Seperate = st.multiselect("Select fields to plot vs Time", options=numeric_cols_Seperate, default=['RPM', 'Fuel PW', 'TPS', 'AFR'], key="seperate")

    # Create subplots
    fig = make_subplots(
        rows=len(selected_cols_Seperate),
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.05,
        subplot_titles=selected_cols_Seperate
    )

    # Add traces
    for i, col in enumerate(selected_cols_Seperate, start=1):
        fig.add_trace(
            go.Scatter(
                x=df['Time'],
                y=df[col],
                mode='lines',
                name=col,
                hoverinfo='x+y+name'
            ),
            row=i,
            col=1
        )
        fig.update_yaxes(title_text=col, row=i, col=1)

    # Layout updates
    fig.update_layout(
        height=300 * len(selected_cols_Seperate),
        xaxis_title="Time (s)",
        template="plotly_white",
        hovermode="x unified",
        showlegend=False
    )

    # Display chart
    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("No Data has been uploaded")