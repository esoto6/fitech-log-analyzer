# Fitech Log Analyzer

The purpose of this project was for 1978 C10 in which I have installed a Fitech 30005 on my truck. However, I have recently been experiencing some issues that I am working on troubleshooting and the handheld has the capability of recording logs. These log outputs are in CSV outputs in which they do not work with their Pro Cal Software. So this tool was created to view and diagnose my current crank no start situation.

## Technologies
- Python
- Pandas
- Streamlit
- Plotly

## How to run locally

>[!NOTES]
>Must have python installed

1. Create Virtual Environment

```python
# Windows
python -m venv .venv

# Linux
python3 -m venv .venv
```

2. Activate Virtual Environment

```python
# Windows 
.venv/scripts/activate

# Linux
source .venv/bin/activate
```

3. Install Required Packages

```python
pip install -r requirements.txt
```

1. Run Streamlit Application

```python
streamlit run app.py
```