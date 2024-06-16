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

def fetchdata():
    conn=createconn()
    cursor=conn.cursor()
    query="select * from student1"
    cursor.execute(query)
    result=cursor.fetchall()
    for i in result:
        print(i)

def updatedata(name,city,sid=0):
    conn=createconn()
    cursor=conn.cursor()
    args=(name,city,sid)
    query="update student1 set name=%s, city=%s where sid=%s"
    cursor.execute(query,args)
    conn.commit()
    print("Record Updated")
    conn.close()

def deletedata(sid):
    conn=createconn()
    cursor=conn.cursor()
    args=(sid)
    query="delete from student1 where sid=%s"
    cursor.execute(query,args)
    conn.commit()
    print("Record Deleted")
    conn.close()

fetchdata()
print("1 for Insert")
print("2 for Update")
print("3 for Delete")
ch=int(input("Enter Your Choice : "))

if ch==1:
    s=int(input("Enter Student ID : "))
    n=input("Enter Student Name : ")
    c=input("Enter City name : ")
    insertdata(s,n,c)
elif ch==2:
    s=int(input("Enter Student ID : "))
    n=input("Enter Student Name : ")
    c=input("Enter City name : ")
    updatedata(n,c,s)
elif ch==3:
    s=int(input("Enter Student ID : "))
    deletedata(s)

fetchdata()