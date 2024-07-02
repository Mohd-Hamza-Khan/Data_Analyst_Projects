import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

df = pd.read_csv("H:\\Data Science\\Data Analyst\\Projects\\Insurance_Web_ML_Prj\\Insurance\\static\\DataSet\\insurance.csv")
df = df.drop_duplicates()

x_axis = ['age', 'bmi', 'children', 'expenses']
for x in x_axis:
    fig, axes = plt.subplots(1,2, figsize=(10,4))
    sns.distplot(df[x], ax = axes[0], kde=False)
    sns.boxplot(df[x], ax=axes[1],orient='h',showmeans=True, color='pink')

df['sex']=df.sex.map({'female':0, 'male':1})
df['smoker']=df.smoker.map({'yes':1,'no':0})
df['region']=df.region.map({'southeast':1,'southwest':2,'northeast':3,'northwest':4})
x = df.drop(['expenses'],axis=1)
y = df[['expenses']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

rf=RandomForestRegressor()
rf.fit(x_train,y_train)
