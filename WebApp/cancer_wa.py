import streamlit as st
import seaborn as sns
import pandas as pd
df_cancer = pd.read_csv("CancerData.csv")
df_mean = df_cancer[df_cancer.columns[:11]]
df_se = df_cancer.iloc[:, [0,11,12,13,14,15,16,17,18,19,20]]
df_worst = df_cancer.iloc[:,[0,21,22,23,24,25,26,27,28,29,30]]

st.title("Breast cancer Web Application")
st.write("Dataframe used:Breast Cancer Diagnostic Classification")

st.write("Select the diagnosis of the cancer that you want to select: ")
checkbox1 = st.checkbox("Benign")
checkbox2 = st.checkbox("Malignant")
dig = 0
if checkbox1:
    val = "Benign"
    dig = 0
elif checkbox2:
    val = "Malignant"
    dig = 1
else:
    val = "Null"
    dig = 2

col_category = {"Mean":df_mean, "Squared Errors":df_se, "Worst":df_worst}
selectbox = st.selectbox("Select the category of features of the cancer mass: ", ["Mean", "Squared Errors", "Worst"])
df_sel = col_category[selectbox]


st.write(f"You selected the diagnosis of the cancer as {val} and its category of features as {selectbox}")

if dig !=2:
    df = df_sel.loc[df_sel['diagnosis'] == dig]
    st.write("\n\n The line graph represented for the {selectbox} of {val} cancer\n")
    st.line_chart(data = df)
else:
    st.write("Missing Selection")




