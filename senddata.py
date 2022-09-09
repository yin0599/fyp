from time import sleep
import mysql.connector

mydb = mysql.connector.connect(#database detail 
  host="localhost",
  user="root",
  password="123456",
  database="example"
)

mycursor =mydb.cursor()#database connection
val = 6 
sql = "INSERT INTO send_data (Number, Movement_data) VALUES (NULL, %i);" % (val)#sql connend for add data 
mycursor.execute(sql)#execute sql commend
print("sent")

mydb.commit()
sleep (2)
val = 1
sql = "INSERT INTO send_data (Number, Movement_data) VALUES (NULL, %i);" % (val)#sql connend for add data 
mycursor.execute(sql)#execute sql commend

mydb.commit()
sleep(5)
val = 9 
sql = "INSERT INTO send_data (Number, Movement_data) VALUES (NULL, %i);" % (val)#sql connend for add data 

mycursor.execute(sql)#execute sql commend
mydb.commit()
sleep(3) 

val = 6 
sql = "INSERT INTO send_data (Number, Movement_data) VALUES (NULL, %i);" % (val)#sql connend for add data 

mycursor.execute(sql)#execute sql commend
mydb.commit()


# val = 6 
# sql = "INSERT INTO send_data (Movement_data) VALUES (%i)" % (val)#sql connend for add data 
# mycursor.execute(sql)#execute sql commend

# mydb.commit()
# sleep (2)
# val = 1
# sql = "INSERT INTO send_data (Movement_data) VALUES (%i)" % (val)
# mycursor.execute(sql)#execute sql commend

# mydb.commit()
# sleep(5)
# val = 9 
# sql = "INSERT INTO send_data (Movement_data) VALUES (%i)" % (val)

# mycursor.execute(sql)#execute sql commend
# mydb.commit()
# sleep(3) 

# val = 6 
# sql = "INSERT INTO send_data (Movement_data) VALUES (%i)" % (val)
