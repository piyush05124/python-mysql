from datetime import time
import mysql
from mysql.connector import connect as cc

db= cc(
      host="localhost",
      user="<your username in server>",
      passwd="<your mysql server password>",
      database="<your database name in the server>"
)

point=db.cursor()

try:
      db.is_connected()
      print("connected")
except ("_mysql_connector.MySQLInterfaceError","mysql.connector.errors.ProgrammingError"):
      print('not connected')



q1="SELECT * from covid ;"
q2="DELETE  FROM covid where state='wb';"
point.execute(q1)

for i in point:
      print(i)

db.commit()


def insert(State,time,Confirmed,Recovered,Deaths,Active):
      s=str(State)
      t=str(time)
      c=float(Confirmed)
      r=float(Recovered)
      d=float(Deaths)
      a=float(Active)
      query="insert into covid(State,time,Confirmed,Recovered,Deaths,Active) values('{}','{}',{},{},{},{} );".format(s,t,c,r,d,a)
      point.execute(query)
      db.commit()
      point.close()

                        
      
      

def update(State,time,Confirmed,Recovered,Deaths,Active):
      s1=str(State)
      t1=str(time)
      c1=float(Confirmed)
      r1=float(Recovered)
      d1=float(Deaths)
      a1=float(Active)
      query1="insert into covid(State,time,Confirmed,Recovered,Deaths,Active) values('{}','{}',{},{},{},{} );".format(s1,t1,c1,r1,d1,a1)
      point.execute(query1)
      db.commit()
      point.close()
      




##def show():
##      querry='select * from covid'
##      
