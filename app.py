import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Titanic Predictor", page_icon="🚢")

model = joblib.load('models/modelo_titanic.pkl')

st.title("Previsão de Sobrevivência - Titanic")
st.markdown("Preencha os dados abaixo para saber se o passageiro sobreviveria.")

col1, col2 = st.columns(2)

with col1:
    pclass = st.selectbox("Classe da Passagem", [1, 2, 3])
    sex = st.radio("Sexo", ["Masculino", "Feminino"])
    age = st.slider("Idade", 0, 100, 25)

with col2:
    sibsp = st.number_input("Irmãos/Cônjuges a bordo", 0, 10, 0)
    parch = st.number_input("Pais/Filhos a bordo", 0, 10, 0)
    fare = st.number_input("Preço da Passagem", 0.0, 512.0, 30.0)

if st.button("Prever Sobrevivência"):
    sex_bin = 1 if sex == "Feminino" else 0
    
    entrada = pd.DataFrame([[pclass, sex_bin, age, sibsp, parch, fare]],
                           columns=['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare'])
    
    predicao = model.predict(entrada)[0]
    probabilidade = model.predict_proba(entrada)[0][1]

    if predicao == 1:
        st.success(f"O passageiro sobreviveria. (Chance: {probabilidade:.2%})")
    else:
        st.error(f"O passageiro não sobreviveria. (Chance: {probabilidade:.2%})")