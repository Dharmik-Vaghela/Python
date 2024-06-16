import pymysql
def createconn():
    return pymysql.connect(host="localhost",database="first",user="root",password="1209",port=3306)

def fetchdata():
    conn=createconn()
    cursor=conn.cursor()
    query="select * from student"
    cursor.execute(query)
    result=cursor.fetchall()
    for i in result:
        print(i)

fetchdata()