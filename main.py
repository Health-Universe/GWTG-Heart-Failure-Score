import streamlit as st
import numpy as np

def calculate_gwtg_hf_risk_score(age, sbp, heart_rate, serum_sodium, creatinine, copd, non_black_race, atrial_fibrillation):
    risk_score = (
        0.487*np.log(age)
        - 0.511*np.log(sbp)
        + 0.730*np.log(heart_rate)
        - 0.529*np.log(serum_sodium)
        + 0.949*np.log(creatinine)
        + 0.636*copd
        + 0.517*non_black_race
        + 0.427*atrial_fibrillation
    )
    return risk_score

st.title("GWTG-Heart Failure Risk Score Calculator")
st.write("Calculate the GWTG-HF Risk Score for in-hospital mortality prediction in heart failure patients.")

age = st.number_input("Age (years)", min_value=18, max_value=120)
sbp = st.number_input("Systolic Blood Pressure (mmHg)", min_value=0, max_value=300)
heart_rate = st.number_input("Heart Rate (beats/min)", min_value=0, max_value=250)
serum_sodium = st.number_input("Serum Sodium (mEq/L)", min_value=100, max_value=200)
creatinine = st.number_input("Creatinine (mg/dL)", min_value=0.0, max_value=15.0, format="%.2f")
copd = st.checkbox("Chronic Obstructive Pulmonary Disease (COPD)")
non_black_race = st.checkbox("Non-Black Race")
atrial_fibrillation = st.checkbox("Atrial Fibrillation")

if st.button("Calculate GWTG-HF Risk Score"):
    risk_score = calculate_gwtg_hf_risk_score(age, sbp, heart_rate, serum_sodium, creatinine, copd, non_black_race, atrial_fibrillation)
    st.write(f"Your GWTG-HF Risk Score is: {risk_score:.2f}")
