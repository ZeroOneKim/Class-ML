from sklearn.linear_model import LogisticRegression
import main
import Query
import pandas as PDS
from sklearn.model_selection import train_test_split

model = LogisticRegression()

result = main.YikimDB.executeQuery(Query.week7_Query)
#print(result)

PDS_DF = PDS.DataFrame(result, columns = ['나이', '음료', '구분'])
#print(PDS_DF)

X = PDS_DF['나이']  #독립
y = PDS_DF['구분']  #종속(0 = 생강/ 1 = 뜨아)

X_train, X_test, y_train, y_test = train_test_split(X.values.reshape(-1, 1), y, test_size=0.2, random_state=50) #Paramter 독립,종속,테스트 세트 비율, 난수패턴(값 아무거나 기입 가능)

model.fit(X_train, y_train)


myAge = 28
for i in range(15):
    LetsGoPredict = model.predict([[myAge]]) #예측
    Accur = model.predict_proba([[myAge]])   #확률

    if LetsGoPredict[0] == 1:
        result = '뜨거운 아메리카노'
    else:
        result = '생강차'

    print(f"{myAge}세 선호: " + result + "      " + str(Accur*100))

    myAge+=2