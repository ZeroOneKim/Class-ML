import pymysql
import info.Security

class YikimDB:
    def executeQuery(query):
        # MySQL 연결부
        con = pymysql.connect(host='localhost', user='root', password=info.Security.password, database='AI_STUDY')
        cursor = con.cursor()

        # 쿼리 실행함
        cursor.execute(query)

        resultData = cursor.fetchall()
        
        cursor.close()
        con.close()

        return resultData
