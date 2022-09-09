import gc
from multiprocessing.sharedctypes import Value
from time import sleep
import mysql.connector
from tkinter import *

get_past_data = 0
current_data = 0
root = Tk() #root of frame
button = 0

entry = Entry(root,width=14, borderwidth=5)#create a box for show the data

mybutton1 = Button(root, text="1", padx=40 ,pady=40 )# frame design
mybutton2 = Button(root, text="2", padx=40 ,pady=40 )
mybutton3 = Button(root, text="3", padx=40 ,pady=40 )
mybutton4 = Button(root, text="4", padx=40 ,pady=40 ) 
mybutton5 = Button(root, text="5", padx=40 ,pady=40 )
mybutton6 = Button(root, text="6", padx=40 ,pady=40 )
mybutton7 = Button(root, text="7", padx=40 ,pady=40 )
mybutton8 = Button(root, text="8", padx=40 ,pady=40 ) 
mybutton9 = Button(root, text="9", padx=40 ,pady=40 )

def set_position():
    entry.grid(row=0 ,column=1)#set the box location
        
    mybutton1.grid(row = 1, column = 1)#set position 
    mybutton2.grid(row = 1, column = 2)
    mybutton3.grid(row = 1, column = 3)
    mybutton4.grid(row = 2, column = 1)
    mybutton5.grid(row = 2, column = 2)
    mybutton6.grid(row = 2, column = 3)
    mybutton7.grid(row = 3, column = 1)
    mybutton8.grid(row = 3, column = 2)
    mybutton9.grid(row = 3, column = 3)       
    
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
        set_position()
        root.mainloop()