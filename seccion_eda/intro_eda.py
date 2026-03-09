import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Análisis Exploratorio de Datos: Introducción")

st.markdown("""
El objetivo de esta sección es entender los datos, qué nos cuentan
Limpiar los datos en caso de ruido, para que el modelo tenga datos relevantes
""")

df = pd.read_csv("diabetes.csv")
st.dataframe(df.head())
