import streamlit as st
import pandas as pd

st.title("Terminology")




@st.cache_data
def load_efi_terms():
    efi_terms = pd.read_csv("data/required/efi_terms.csv")
    return efi_terms

@st.cache_data
def load_efi_params():
    efi_params = pd.read_csv("data/required/efi_paramaters.csv")
    return efi_params


efi_terms = load_efi_terms()
efi_params = load_efi_params()


st.write("# EFI Basic Terms")
for idx, row in efi_terms.iterrows():
    if idx == 0:
        pass
    else:
        st.write(f"### **{row['Term']}**")
        st.write(f"{row['Definition']}")

st.write("# EFI Parameters")
for idx, row in efi_params.iterrows():
    if idx == 0:
        pass
    else:
        st.write(f"### **{row['Parameter']}**")
        st.write(f"Meaning:")
        st.write(f"{row['Meaning']}")
        
        st.write(f"Normal Range / Behavior")
        st.write(f"{row['Normal Range / Behavior']}")

        st.write("Notes:")
        st.write(f"{row['Notes']}")


