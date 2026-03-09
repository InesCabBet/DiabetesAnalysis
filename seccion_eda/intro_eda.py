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

st.markdown("## **Descripción de las variables del dataset**")
st.markdown("""
- **Pregnancies** → Número de embarazos que ha tenido la persona. Cambios hormonales y metabólicos durante el embarazo pueden influir en el riesgo de desarrollar diabetes.

- **Glucose** → Nivel de glucosa en sangre. Es uno de los indicadores más importantes, ya que niveles elevados de glucosa suelen estar directamente relacionados con la diabetes.

- **BloodPressure** → Presión arterial diastólica. Problemas metabólicos como la diabetes suelen estar asociados con alteraciones en la presión sanguínea.

- **SkinThickness** → Grosor del pliegue cutáneo del tríceps. Se utiliza como una medida indirecta de la grasa corporal, que puede estar relacionada con problemas metabólicos.

- **Insulin** → Nivel de insulina en sangre. La insulina es la hormona que regula la glucosa; alteraciones en su nivel pueden indicar problemas en el metabolismo del azúcar.

- **BMI** → Índice de Masa Corporal (Body Mass Index). Es una medida que relaciona peso y altura y permite estimar si una persona tiene sobrepeso u obesidad, factores asociados con la diabetes.

- **DiabetesPedigreeFunction** → Medida que representa la predisposición genética a la diabetes basada en el historial familiar.

- **Age** → Edad del paciente. El riesgo de desarrollar diabetes suele aumentar con la edad.

- **Outcome** → Indica si el paciente tiene diabetes (1) o no (0). Esta es la **variable objetivo** que el modelo intenta predecir.
""")

df = pd.read_csv("diabetes.csv")
st.dataframe(df.head(10))

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
