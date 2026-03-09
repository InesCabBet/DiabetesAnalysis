import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("diabetes.csv")

st.title("Análisis Exploratorio de Datos: Estadísticos Básicos")

st.markdown("### Datos sobre el dataset")
st.dataframe(df.describe().T)

st.markdown("### Distribución de las variables")
