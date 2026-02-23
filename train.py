import panda as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv('titanic.csv')

features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
x = df[features].copy()
y=df['Survived']

x['Age'] = x['Age'].fillna(x['Age'].median())
x['Fare'] = x['Fare'].fillna(x['Fare'].median())
x['Sex'] = x['Sex'].map({'male':0, 'female':1})

modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(x, y)

joblib.dump(modelo, 'models/modelo_titanic.pkl')