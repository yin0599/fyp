import gc
from multiprocessing.sharedctypes import Value
from time import sleep
import mysql.connector
from tkinter import *

root = Tk()
root.title('testing size gui')
root.geometry("500x500")#GUI size
get_past_data = 0
current_data = 0
button = 0

# Grid.rowconfigure(root, 0 , weight = 1)
# Grid.columnconfigure(root, 0 , weight = 1)
# row2
# Grid.rowconfigure(root, 1 , weight = 1)

mybutton1 = Button(root,text="Button 1")
mybutton2 = Button(root,text="Button 2")
mybutton3 = Button(root,text="Button 3")
mybutton4 = Button(root,text="Button 4")
mybutton5 = Button(root,text="Button 5")
mybutton6 = Button(root,text="Button 6")
mybutton7 = Button(root,text="Button 7")
mybutton8 = Button(root,text="Button 8")
mybutton9 = Button(root,text="Button 9")

entry = Entry(root,width=3, borderwidth=5)
entry.grid(row = 0, column=1)
mybutton1.grid(row = 1, column = 1,sticky="nsew")#set position 
mybutton2.grid(row = 1, column = 2,sticky="nsew")
mybutton3.grid(row = 1, column = 3,sticky="nsew")
mybutton4.grid(row = 2, column = 1,sticky="nsew")
mybutton5.grid(row = 2, column = 2,sticky="nsew")
mybutton6.grid(row = 2, column = 3,sticky="nsew")
mybutton7.grid(row = 3, column = 1,sticky="nsew")
mybutton8.grid(row = 3, column = 2,sticky="nsew")
mybutton9.grid(row = 3, column = 3,sticky="nsew")  

mybuttonlist_row = [mybutton1 ,mybutton2,mybutton3]
mybuttonlist_column = [mybutton1,mybutton4,mybutton7]

row_number = 1
column_number = 1

for button in mybuttonlist_row:
        Grid.columnconfigure(root, column_number, weight= 1)
        column_number += 1

for button in mybuttonlist_column:
        Grid.rowconfigure(root, row_number, weight= 1)
        row_number += 1


def checkused():# check function 
    global button

    match(str(get_past_data)) : #case to change color
        case '1':
                return mybutton1.configure(background='SystemButtonFace')
        case '2':
                return mybutton2.configure(background='SystemButtonFace')
        case '3':
                return mybutton3.configure(background='SystemButtonFace')
        case '4':
                return mybutton4.configure(background='SystemButtonFace')
        case '5':
                return mybutton5.configure(background='SystemButtonFace')
        case '6':
                return mybutton6.configure(background='SystemButtonFace')
        case '7':               
                return mybutton7.configure(background='SystemButtonFace')
        case'8':
                return mybutton8.configure(background='SystemButtonFace')
        case '9':
                return mybutton9.configure(background='SystemButtonFace')


def button_click(number):#get button location to change color
    current = input.get()
    input.delete(0,END)
    input.insert(0,str(number))#display data
    return 

def ChangeColor(num): #current data to get location
    global get_past_data,current_data

    if get_past_data != current_data:
        checkused()
    else:  
        match(str(num)):
            case '1':
                return mybutton1.configure(background='green')
            case '2':
                return mybutton2.configure(background='green')
            case '3':
                return mybutton3.configure(background='green')
            case '4':
                return mybutton4.configure(background='green')
            case '5':
                return mybutton5.configure(background='green')
            case '6':
                return mybutton6.configure(background='green')
            case '7':
                return mybutton7.configure(background='green')
            case '8':
                return mybutton8.configure(background='green')
            case '9':
                return mybutton9.configure(background='green')

def get_database_data():
    global current_data, get_past_data 
    mydb = mysql.connector.connect(#database detail
    host="localhost",
    user="root",
    password="123456",
    database="example"
    ) 
    gc.collect()   
    sqlite_select_query = """SELECT Number, movement_data FROM `send_data` ORDER BY Number DESC LIMIT 1;""" #get the last data
    mydb.connect()
    mycursor = mydb.cursor()#get conncetion 
    root.after(10, get_database_data)# for keeping lopp
            
     
    mycursor.execute(sqlite_select_query) #execute the sql commond
    records = mycursor.fetchall()#get data

    for records in records:# display data
        print("id: ", records[0])
        print("data: ", records[1])
        print("\n")
    entry.delete(0,END) #delete pervious value 
    entry.insert(0,str(records[1]))#set value to box
    get_past_data = current_data
    current_data = records[1]

    ChangeColor(current_data)
    mydb.close()

while True:
        get_database_data()#for get data
        root.mainloop()