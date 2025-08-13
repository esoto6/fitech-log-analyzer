import streamlit as st

st.title("Terminology")

automotive_terms = [
    'RPM', 'MAP', 'Coolant Temp', 'AFR', 'Target AFR', 'Lambda',
    'Lambda Target', 'AFR Trim %', 'AFR Learn %', 'Idle Fuel Learn',
    'Fans On', 'TPS', 'Fuel PW', 'Inject Duty%', 'MAP Fueled',
    'Transient Fuel', 'Target RPM', 'IAC Steps', 'Idle PID', 'Fuel Pump',
    'Fuel Flowrate', 'Air Temp', 'Cylinder Temp', 'Battery', 'BARO',
    'WBO2 Temp', 'Warmup%', 'Startup%', 'Run Rev', 'Run State', 'Fault1',
    'Fault2', 'Fault3', 'Save Fault', 'Save Fault.1', 'Gear State',
    'vehicle speed'
]

for col in automotive_terms:
    st.write(
        f"## **{col}**: "
    )
