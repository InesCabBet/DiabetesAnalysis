import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Análisis Exploratorio de Datos: Introducción")

st.markdown("""
El objetivo de esta sección es entender los datos, qué nos cuentan.
Limpiar los datos en caso de ruido, para que el modelo tenga datos relevantes
""")

df = pd.read_csv("diabetes.csv")
st.dataframe(df.head(10))
st.dataframe(df.info())


st.markdown("""
Podemos observar que hay datos a 0 pero que es fisiológicamente imposible que lo estén. 
Entiendo que son datos faltantes, es por ello que cambiaré dichos datos por la mediana en las columnas afectadas, que son:
            1. Glucose 
            2. Insulin
            3. BMI
            4. BloodPresure
            5. SkinThickness""")

cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
df[cols] = df[cols].replace(0, np.nan)

df['Glucose'] = df['Glucose'].fillna(df['Glucose'].median())
df['BloodPressure'] = df['BloodPressure'].fillna(df['BloodPressure'].median())
df['SkinThickness'] = df['SkinThickness'].fillna(df['SkinThickness'].median())
df['Insulin'] = df['Insulin'].fillna(df['Insulin'].median())
df['BMI'] = df['BMI'].fillna(df['BMI'].median())

st.markdown("### Datos Limpios")
st.dataframe(df.head(10))

st.markdown("### Datos sobre el dataset")
st.dataframe(df.describe().T)