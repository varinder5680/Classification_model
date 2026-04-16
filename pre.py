import streamlit as st
import pandas as pd
import joblib 

model=joblib.load("logistic.pkl")
scaler=joblib.load("scaler.pkl")
expected_columns=joblib.load("coumns.pkl")
import pandas as pd
import joblib 

model=joblib.load("logistic.pkl")
scaler=joblib.load("scaler.pkl")
expected_columns=joblib.load("coumns.pkl")

st.title("heart_prediction_user")

st.markdown("provide details")

age=st.slider("Age", 18,100,40)
Sex=st.selectbox("Sex", ["M","F"])
Chest_pain=st.selectbox("chest pain type", ["ATA", "NAP", "TA", "ASY"])
RestingBP=st.number_input("resing bp (MM HG)", 80,200)
Cholesterol=st.number_input("Cholesterol (md/dl)", 100,600,200)
FastingBS=st.selectbox("Fasing blood suger > 120 mg/dl", [0,1])
resting_ecg=st.selectbox("Resting ecg", ["Normal", "ST", "LVH"])
mx_hr=st.slider("Max hR", 60, 220, 150)
ExerciseAngina=st.selectbox("Exercise Angina ", ["Yes","NO"])
Oldpeak=st.slider("oldpeak (st_depression) ", 0.0,6.0, 1.0)
st_slope=st.selectbox("St Slope", ["UP", "Flat", "Down"])

if st.button("Predict"):
    raw_input={
    'Age': age,
    'RestingBP': RestingBP,
    'Cholesterol':Cholesterol ,
    'FastingBS': FastingBS,
    'MaxHR': mx_hr,
    'Oldpeak': Oldpeak,
    'Sex_' + Sex: 1,
    'ChestPainType_' + Chest_pain: 1,
    'RestingECG_' + resting_ecg: 1,
    'ExerciseAngina_' + ExerciseAngina: 1,
    'ST_Slope_' + st_slope: 1
}
    input_df=pd.DataFrame([raw_input])
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col]=0
    input_df=input_df[expected_columns]
    scale_input=scaler.transform(input_df)
    prediction=model.predict(scale_input)[0]
    if prediction == 1:
            st.error("HIgh risk heart attack")
    else:
            ("Low Risk of ATTAK")

