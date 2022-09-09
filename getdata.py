from time import sleep
import mysql.connector


mydb = mysql.connector.connect(#database detail
  host="localhost",
  user="root",
  password="123456",
  database="example"
)    
sqlite_select_query = """SELECT no, movement_data FROM `send_data` ORDER BY no DESC LIMIT 1;""" #get the last data
while True:# keep looping
  try:
    mydb.connect()
    mycursor = mydb.cursor()#get conncetion 

  # mycursor.execute("SHOW TABLES")
  # print(mycursor)
    

    mycursor.execute(sqlite_select_query) #execute the sql commond
    records = mycursor.fetchall()
        
    for i in records:# loop data 
      print("id: ", i[0])
      print("data: ", i[1])
      print("\n")

    sleep(1)
    mydb.close()    
  except:
    print("Something went wrong")
    break

  print(mycursor.rowcount, "record inserted.")# count the data 
