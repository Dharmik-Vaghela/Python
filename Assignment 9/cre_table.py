import pymysql
def createconn():
    return pymysql.connect(host="localhost",database="first",user="root",password="1209",port=3306)

def createtable():
    conn=createconn()
    cursor=conn.cursor()
    query="create table student1(sid int primary key, name VARCHAR(50), city VARCHAR(50))"
    cursor.execute(query)
    conn.commit()
    print("Table Created")
    conn.close()

createtable()