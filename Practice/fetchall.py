import pymysql
def createconn():
    return pymysql.connect(host="localhost",database="first",user="root",password="",port=3306)
def fetchall(sid):
    conn=createconn()
    cursor=conn.cursor()
    args=(sid)
    query="select * from student where sid=%s"
    cursor.execute(query)
    result=cursor.fetchall()
    for i in result:
        print(i)

fetchall()