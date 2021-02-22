import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as c
# definitions
# 1
def columns():
    global tree,cols
    tree.grid(row=3,column=0,columnspan=10)
    tree.heading('#0', text='Sno')
    verscrlbar = ttk.Scrollbar(root1,orient ="vertical",command = tree.yview)
    verscrlbar.grid(column=11,row=2,rowspan=11)
    tree.column('#0', minwidth=0, width=110,stretch=False, anchor ='c') 
    def hc():
        for i in range(0,len(cols)):
            tree.heading(f'#{i+1}', text=cols[i])
            tree.column(f'#{i+1}', minwidth=0, width=100,stretch=True, anchor ='c') 
    hc()
# 2
def dblist():
    record = mycursor.fetchall()
    n=[]
    x=0
    for row in record:
        t=[]
        for i in row:
            if i=='\n':    
                t.append('none')
            else:
                t.append(i)
        if x>=0:
            n.append(t)
        x+=1
    return n
# 3
def displaytable(val,x):
    global tree,cols
    tree.insert(parent='', index=tk.END, iid=x, text=val[0], values=val[1:])
# 4
x=0
def display1(y,p):
    global mycursor,x,p1
    mycursor.execute(f"SELECT * FROM {y} where Order_expectation='{p}'")
    p1=dblist()
    x=0
    for i in p1:
        displaytable(tuple(i),x)
        x+=1
def display(p):
    global mycursor,x,p1
    mycursor.execute(f"SELECT * FROM {p}")
    p1=dblist()
    x=0
    for i in p1:
        displaytable(tuple(i),x)
        x+=1
# 5
def delete():
    tree.delete(*tree.get_children())
# 6
def c1():
    delete()
    display1('order_pending','C1')
# 7
def c2():
    delete()
    display1('order_pending','C2')
# 8
def c3():
    delete()
    display1('order_pending','C3')
# 9
def focus(event): 
    global mycursor,widget,al
    widget = int(tree.focus())
    print(widget,"has focus")
    al=p1[widget]
# 10
def removeheadval(new):
    global al
    mycursor.execute(f"delete from {new} where Sno={al[0]}")
    mydb.commit()
# 11
def tranfer_to_order_won():
    MsgBox = tk.messagebox.askquestion('Transfer to Order won','Do you want to transfer the selected row to Order won?',icon = 'warning')
    msg1('order_won',MsgBox)
# 12
def tranfer_to_order_pending():
    MsgBox = tk.messagebox.askquestion('Transfer to Order pending','Do you want to transfer the selected row to Order pending?',icon = 'warning')
    msg1('order_pending',MsgBox)   
# 13
def order_won():
    delete()
    display('order_won')
# 14
def order_pending():
    delete()
    display('order_pending')
# 15
def order_lost():
    delete()
    display('order_lost')
# 16
def ExitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
        root1.destroy()
    else:
        tk.messagebox.showinfo('Return','You will now return to the application screen')
# 17
def allstar():
    delete()
    display('head')
# 18
def msg1(new,MsgBox):
    global al
    if MsgBox=='yes':
        tab=['order_won','order_lost','order_pending']
        
        mycursor.execute(f'select * from {new} where Sno={al[0]}')
        if dblist()==[]:
            mycursor.execute(f"insert into {new} values({al[0]},'{al[1]}',{al[2]},{al[3]},{al[4]},'{al[5]}',{al[6]},'{al[7]}','{al[8]}','{al[9]}','{al[10]}')")
            mydb.commit()
            tab.remove(new)
            for i in tab:
                mycursor.execute(f'select * from {i} where Sno={al[0]}')
                if dblist()!=[]:
                    removeheadval(i)
            tk.messagebox.showinfo('Return','The value has been successfully tranferred (Press display button to view the refreshed value)')
        else:
            tk.messagebox.showinfo('Return',f'The value is already present in {new}')
    else:
        tk.messagebox.showinfo('Return','The value wasn\'t tranferred')  
# 19
def tranfer_to_order_lost():
    MsgBox = tk.messagebox.askquestion('Transfer to Order lost','Do you want to transfer the selected row to Order lost?',icon = 'warning')
    msg1('order_lost',MsgBox)
# 20
def transfer_c(c):
    for i in ['head','order_won','order_lost','order_pending']:
        mycursor.execute(f'select * from {i} where Sno={al[0]}')
        if dblist()!=[]:
            mycursor.execute(f"update {i} set Order_expectation='{c}' where Sno={al[0]}")
#21
def transfer_c1():
    msg2('C1')
#22
def transfer_c2():
    msg2('C2')
#23 
def transfer_c3():
    msg2('C3')
# 24
def msg2(new):
    MsgBox = tk.messagebox.askquestion(f'Transfer to {new}',f'Do you want to transfer the selected row to {new}?',icon = 'warning')
    if MsgBox=='yes':
        transfer_c(new)
        tk.messagebox.showinfo('Return','The value has been successfully tranferred (Press display button to view the refreshed value)')
    else:
        tk.messagebox.showinfo('Return','The value wasn\'t tranferred')

root1=tk.Tk()
root1.geometry('1150x430')
root1.title('RMH Enquiry update')
root1.iconbitmap(r"/Users/neshaa.laksh/Downloads/Elegantthemes-Beautiful-Flat-Document.ico")  
mydb = c.connect(host="localhost",user="root", password="9626422742",database="rmh")
mycursor = mydb.cursor()
cols = ('Name', 'Date','Month','Year','City','Whatsapp num','Product type','Model','c','Remarks')
tree = ttk.Treeview(root1, selectmode="browse", columns=cols)
columns()
comp_name1=tk.Label(root1,text=' RMH Corporation ' ,font='verdana 27',bg='orange')
comp_name1.grid(row=0,column=0,sticky='n',columnspan=3,padx=10,pady=10)

comp_name2=tk.Label(root1,text='Enquiry update' ,font='verdana 23',bg='light blue')
comp_name2.grid(row=1,column=0,sticky='n',columnspan=3,padx=10,pady=10)

comp_name3=tk.Label(root1,text='Window' ,font='verdana 23',bg='light blue')
comp_name3.grid(row=2,column=0,sticky='n',columnspan=3,padx=10,pady=10)

b11=tk.Button(root1,text='Transfer to C1',font='verdana 15',command=transfer_c1)
b11.grid(row=0,column=3,sticky='nesw',padx=10,pady=10)

b12=tk.Button(root1,text='Transfer to C2',font='verdana 15',command=transfer_c2)
b12.grid(row=1,column=3,sticky='nesw',padx=10,pady=10)

b13=tk.Button(root1,text='Transfer to C3',font='verdana 15',command=transfer_c3)
b13.grid(row=2,column=3,sticky='nesw',padx=10,pady=10)

b1=tk.Button(root1,text='Display C1',font='verdana 15',command=c1)
b1.grid(row=0,column=5,sticky='nesw',padx=10,pady=10)
b2=tk.Button(root1,text='Display C2',font='verdana 15',command=c2)
b2.grid(row=0,column=7,sticky='nesw',padx=10,pady=10)
b3=tk.Button(root1,text='Display C3',font='verdana 15',command=c3)
b3.grid(row=0,column=9,sticky='nesw',padx=10,pady=10)
b4=tk.Button(root1,text='Transfer to order won',font='verdana 15',command=tranfer_to_order_won)
b4.grid(row=1,column=5,sticky='nesw',padx=10,pady=10)
b5=tk.Button(root1,text='Transfer to order pending',font='verdana 15',command=tranfer_to_order_pending)
b5.grid(row=1,column=7,sticky='nesw',padx=10,pady=10)
b6=tk.Button(root1,text='Transfer to order lost',font='verdana 15',command=tranfer_to_order_lost)
b6.grid(row=1,column=9,sticky='nesw',padx=10,pady=10)
b7=tk.Button(root1,text='Display order won',font='verdana 15',command=order_won)
b7.grid(row=2,column=5,sticky='nesw',padx=10,pady=10)
b8=tk.Button(root1,text='Display order pending',font='verdana 15',command=order_pending)
b8.grid(row=2,column=7,sticky='nesw',padx=10,pady=10)
b9=tk.Button(root1,text='Display order lost',font='verdana 15',command=order_lost)
b9.grid(row=2,column=9,sticky='nesw',padx=10,pady=10)
tree.bind("<Button-1>", lambda e: focus(e))
b10=tk.Button(root1,highlightbackground="Red",text='Display all',font='verdana 15',command=allstar)
b10.grid(row=10,column=7,sticky='nesw',padx=10,pady=10)
butt=tk.Button(root1,highlightbackground="Yellow",text='Done',command=ExitApplication,font='verdana 15')
butt.grid(row=10,column=9,sticky='nesw',padx=10,pady=10)

root1.mainloop()
