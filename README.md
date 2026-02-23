# 🚢 Titanic Survival Predictor - Streamlit

Este projeto foi desenvolvido como parte das atividades práticas de Data Science do **CentroWeg**. O objetivo é criar uma aplicação interativa que utiliza um modelo de Machine Learning para prever a sobrevivência de um passageiro no naufrágio do Titanic com base em atributos como idade, sexo, classe da passagem e tarifa.

## 👨‍💻 Informações do Aluno
* **Nome:** Vinícius de Figueiredo Anacleto
* **Turma:** MIDS-78
* **Professor:** João Pedro Silva Valentim
* **Instituição:** CentroWeg

---

## 🛠️ Estrutura do Projeto

O repositório está organizado da seguinte forma:

* `data/`: Contém os datasets originais (Kaggle).
* `models/`: Contém o modelo treinado salvo em formato `.pkl`.
* `train.py`: Script Python responsável pelo pré-processamento dos dados e treinamento do modelo Random Forest.
* `app.py`: Script que contém a interface interativa desenvolvida em Streamlit.
* `requirements.txt`: Lista de bibliotecas necessárias para a execução do projeto.

---

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos
Certifique-se de ter o Python instalado. Recomenda-se criar um ambiente virtual.

### 2. Instalação das Dependências
No terminal, instale as bibliotecas necessárias:
```bash
pip install -r requirements.txt
```

### 3. Treinar o Modelo
Antes de rodar o app, é necessário gerar o arquivo do modelo treinado:
```Bash
python train.py
```

### 4. Rodar a Interface Streamlit
Após gerar o modelo na pasta models/, execute a aplicação:
```Bash
python -m streamlit run app.py
```

🧠 Tecnologias Utilizadas
- Python: Linguagem principal.
- Pandas: Manipulação e análise de dados.
- Scikit-Learn: Treinamento do modelo classificatório (Random Forest).
- Joblib: Persistência do modelo treinado.
- Streamlit: Criação da interface web interativa.

📊 Dataset
Os dados utilizados foram extraídos da competição oficial: [Titanic - Machine Learning from Disaster](https://www.kaggle.com/competitions/titanic/data) Kaggle.


