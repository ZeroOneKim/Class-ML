week5_Query = "SELECT A.SELL_ID, A.AGE, A.DRINK, A.YMDATE, B.TEMPERATURE, B.WEATHER_STATE, C.PRICE FROM SELL_LOG A JOIN WEATHER_DATA B ON A.YMDATE = B.YMDATE JOIN PRICE C ON A.DRINK = C.DRINK"

week7_Query = "SELECT AGE, DRINK, IF(DRINK = '생강차', 0, 1) as NUM FROM SELL_LOG WHERE DRINK IN('핫 아메리카노', '생강차')"