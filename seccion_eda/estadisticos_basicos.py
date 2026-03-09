import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("diabetes.csv")
cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
df[cols] = df[cols].replace(0, np.nan)

df['Glucose'] = df['Glucose'].fillna(df['Glucose'].median())
df['BloodPressure'] = df['BloodPressure'].fillna(df['BloodPressure'].median())
df['SkinThickness'] = df['SkinThickness'].fillna(df['SkinThickness'].median())
df['Insulin'] = df['Insulin'].fillna(df['Insulin'].median())
df['BMI'] = df['BMI'].fillna(df['BMI'].median())

st.title("Análisis Exploratorio de Datos: Estadísticos Básicos")

st.markdown("### Datos sobre el dataset")
st.dataframe(df.describe().T)

st.markdown("### Distribución de las variables")
cols = st.columns(7)

with cols[0]:
    fig, ax = plt.subplots()
    sns.histplot(df['Pregnancies'], kde=True)
    plt.title("Distribución de Embarazos")
    st.pyplot(fig)

with cols[1]:
    fig, ax = plt.subplots()
    sns.histplot(df['Glucose'], kde=True)
    plt.title("Distribución de Glucosa")
    st.pyplot(fig)

with cols[2]:
    fig, ax = plt.subplots()
    sns.histplot(df['BloodPressure'], kde=True)
    plt.title("Distribución de Presión en Sangre")
    st.pyplot(fig)

with cols[3]:
    fig, ax = plt.subplots()
    sns.histplot(df['SkinThickness'], kde=True)
    plt.title("Distribución de SkinThickness")
    st.pyplot(fig)

st.markdown("---")

with cols[4]:
    fig, ax = plt.subplots()
    sns.histplot(df['Insulin'], kde=True)
    plt.title("Distribución de Insulina")
    st.pyplot(fig)

with cols[5]:
    fig, ax = plt.subplots()
    sns.histplot(df['BMI'], kde=True)
    plt.title("Distribución de BMI")
    st.pyplot(fig)

with cols[6]:
    fig, ax = plt.subplots()
    sns.histplot(df['DiabetesPedigreeFunction'], kde=True)
    plt.title("Distribución de DiabetesPedigreeFunction")
    st.pyplot(fig)

st.markdown("---")

with cols[7]:
    fig, ax = plt.subplots()
    sns.histplot(df['Age'], kde=True)
    plt.title("Distribución de Edad")
    st.pyplot(fig)