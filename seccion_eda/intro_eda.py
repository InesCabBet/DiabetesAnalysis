import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Análisis Exploratorio de Datos: Introducción")

st.markdown("""
El objetivo de esta sección es entender los datos, qué nos cuentan.
Limpiar los datos en caso de ruido, para que el modelo tenga datos relevantes
""")

df = pd.read_csv("diabetes.csv")
st.dataframe(df.head(10))

st.markdown("""
Podemos observar que hay datos a 0 pero que es fisiológicamente imposible que lo estén. 
Entiendo que son datos faltantes, es por ello que cambiaré dichos datos por la mediana en las columnas afectadas, que son:
            1. Glucose 
            2. Insulin
            3. BMI
            4. BloodPresure""")
