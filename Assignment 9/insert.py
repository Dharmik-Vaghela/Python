import pymysql
def createconn():
    return pymysql.connect(host="localhost",database="first",user="root",password="1209",port=3306)

def insertdata(sid,name,city):
    conn=createconn()
    cursor=conn.cursor()
    args=(sid,name,city)
    query="insert into student1(sid,name,city) values(%s,%s,%s)"
    cursor.execute(query,args)
    conn.commit()
    print("Record Inserted")
    conn.close()

i=int(input("Enter Student ID : "))
n=input("Enter Your name : ")
c=input("Enter Your City : ")
insertdata(i,n,c)