from sklearn.linear_model import LogisticRegression
import main
import Query
import pandas as PDS
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import warnings

warnings.filterwarnings("ignore", category=UserWarning)
model = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=200)

result = main.YikimDB.executeQuery(Query.week8_Query)
#print(result)

PDS_DF = PDS.DataFrame(result, columns = ['나이', '음료', '구분', '기온'])
#print(PDS_DF)

X = PDS_DF[['나이', '기온']]  #독립
y = PDS_DF['구분']  #종속(0 = 생강/ 1 = 뜨아/ 2 = 카페라떼, 3 = 스무디, 4 = 아아)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=50) #Paramter 독립,종속,테스트 세트 비율, 난수패턴(값 아무거나 기입 가능)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"모델의 정확도: {accuracy * 100:.2f}%")

predicted_result = model.predict([[55, -7]])

print(f"예측 결과 : {predicted_result[0]}")
#(0 = 생강/ 1 = 뜨아/ 2 = 카페라떼, 3 = 스무디, 4 = 아아)

print(model.predict_proba([[55,-7]])*100)