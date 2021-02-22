import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='9626422742',db='rmh')
mycursor = mydb.cursor()
#creating table head where all values will be there
head="create table head(Sno bigint(10),Name varchar(1000),Date bigint(8),Month bigint(3),Year bigint(5),City varchar(1000),Whatsappnum bigint(20),Product_type varchar(1000),Model varchar(1000),Order_expectation varchar(1000),Remarks varchar(10000))"
mycursor.execute(head)
mydb.commit()
#creating table order_won where only values of order won will be there
order_won="create table order_won(Sno bigint(10),Name varchar(1000),Date bigint(8),Month bigint(3),Year bigint(5),City varchar(1000),Whatsappnum bigint(20),Product_type varchar(1000),Model varchar(1000),Order_expectation varchar(1000),Remarks varchar(10000))"
mycursor.execute(order_won)
mydb.commit()
#creating table order_pending where only values of order pending will be there
order_pending="create table order_pending(Sno bigint(10),Name varchar(1000),Date bigint(8),Month bigint(3),Year bigint(5),City varchar(1000),Whatsappnum bigint(20),Product_type varchar(1000),Model varchar(1000),Order_expectation varchar(1000),Remarks varchar(10000))"
mycursor.execute(order_pending)
mydb.commit()
#creating table order_lost where only values of order lost will be there
order_lost="create table order_lost(Sno bigint(10),Name varchar(1000),Date bigint(8),Month bigint(3),Year bigint(5),City varchar(1000),Whatsappnum bigint(20),Product_type varchar(1000),Model varchar(1000),Order_expectation varchar(1000),Remarks varchar(10000))"
mycursor.execute(order_lost)
mydb.commit()

sno,name,d,m,y,city,wphn,dp,mt,c,r=0,'None',1,1,20,'None',12345678,'None','None','c','None'

mycursor.execute(f"insert into order_won values({sno},'{name}',{d},{m},{y},'{city}',{wphn},'{dp}','{mt}','{c}','{r}')")
mydb.commit()
mycursor.execute(f"insert into order_lost values({sno},'{name}',{d},{m},{y},'{city}',{wphn},'{dp}','{mt}','{c}','{r}')")
mydb.commit()
mycursor.execute(f"insert into order_pending values({sno},'{name}',{d},{m},{y},'{city}',{wphn},'{dp}','{mt}','{c}','{r}')")
mydb.commit()
mycursor.execute(f"insert into head values({sno},'{name}',{d},{m},{y},'{city}',{wphn},'{dp}','{mt}','{c}','{r}')")
mydb.commit()
mycursor.execute('show tables')
for x in mycursor:
  print(x)
mycursor.execute('select * from head')
for x in mycursor:
  print(x)
mycursor.execute('select * from order_won')
for x in mycursor:
  print(x)
mycursor.execute('select * from order_pending')
for x in mycursor:
  print(x)
mycursor.execute('select * from order_lost')
for x in mycursor:
  print(x)