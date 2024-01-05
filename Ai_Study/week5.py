import main
import Query
import pandas as PDS

PDS_DF = PDS.DataFrame(main.YikimDB.executeQuery(Query.week5_Query), columns=['SELL_ID', 'AGE', 'DRINK', 'DATE', 'TEMPERATURE', 'WEATHER_STATE', 'PRICE'])

RES_DF = PDS_DF.groupby(['DATE', 'WEATHER_STATE'])['PRICE'].sum()
#RES_DF[RES_DF['WEATHER_STATE'] == '맑음']   => 'WEATHER_STATE' 컬럼이 인덱스에 존재하므로 인덱스로 접근해야 했다. 
# 참고 : https://makeit.tistory.com/117

#print(RES_DF.index.get_level_values('WEATHER_STATE') == '맑음')
print(RES_DF[RES_DF.index.get_level_values('WEATHER_STATE') == '맑음'].mean())  #맑음에 대한 평균

#print('INDEX : ' + RES_DF.index.get_level_values(0))  COL 접근
#print(PDS_DF.groupby(['DATE'])['PRICE'].sum())

#익숙한 avg()가 아닌 mean()이 평균을 계산함!
_AVG = RES_DF[RES_DF.index.get_level_values('WEATHER_STATE') == '맑음'].mean()

addData = PDS.DataFrame({
    'WEATHER_STATE': ['맑음', '맑음'],
    'PRICE': [_AVG, _AVG]
}, index=['2023-12-18', '2023-12-19'])


RES_DF2 = PDS.concat([RES_DF, addData['PRICE'].astype(int)])

print(RES_DF2)
print('---평균 수익---')
print(RES_DF2.mean())

