import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import date
from tkinter.scrolledtext import ScrolledText
import mysql.connector as c
mydb=c.connect(host='localhost',user='root',password='9626422742',database='rmh')
mycursor=mydb.cursor()

#definitions

def callback(eventObject):
    abc = eventObject.widget.get()
    dpp= dp.get()
    index=product_type.index(dpp)
    mt.config(values=model_types[index])

def textbox(r):
    text=tk.Entry(bd=5,width=39)
    text.grid(row=r,column=1,sticky='nw',padx=10,pady=10)
    return text.get()

def label(t,r):
    label=tk.Label(root,text=t,font='verdana 20',bg='orange')
    label.grid(row=r,column=0,sticky='nw',padx=10,pady=10)

def ExitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
        today = date.today()
        d=today.strftime('%d')
        m=today.strftime('%m')
        y=today.strftime('20'+'%y')
        sno=mycursor.execute('select max(sno) from head')
        for x in mycursor:
            sno=int(x[0])+1
        mycursor.execute(f"insert into order_pending values({sno},'{name_textbox.get()}',{d},{m},{y},'{city_textbox.get()}',{wphn_textbox.get()},'{dp.get()}','{mt.get()}','{c.get()}','{st.get(1.0,tk.END)}')")
        mydb.commit()
        mycursor.execute(f"insert into head values({sno},'{name_textbox.get()}',{d},{m},{y},'{city_textbox.get()}',{wphn_textbox.get()},'{dp.get()}','{mt.get()}','{c.get()}','{st.get(1.0,tk.END)}')")
        mydb.commit()
        

        root.destroy()
    else:
        tk.messagebox.showinfo('Return','You will now return to the application screen')
    
#end
root=tk.Tk()
root.title('RMH Customer Management')
root.configure(bg='orange')

root.iconbitmap(r"/Users/neshaa.laksh/Downloads/Elegantthemes-Beautiful-Flat-Document.ico")

product_type=['Engines',
            'Pumps',
            'Alternators',
            'Open Gensets',
            'Portable Gensets',
            'Silent Gensets',
            'Fuel Pumpsets',
            'Electric Pumpsets',
            'Motors',
            'Power Tiller',
            'Brush Cutter',
            'Any Other (type in the next box)']
model_type_Engines=['Koel','Honda','Eicher']
model_type_Pumps=['NW','Sp3L','Other(type here)']
model_type_Alternators=['single phase','3 phase']
model_type_OpenGensets=['5 kva','7.5 kva','10 kva','15 kva']
model_type_PortableGensets=['850 w','2000 w', '3000 w', '4000 w', '6000 w']
model_type_SilentGensets=['upto 15 kva','20-35kva' , '40-125 kva', 'above 125kva']
model_type_FuelPumpsets=['honda','koel portable', 'Koel AV & SV']
model_type_ElectricPumpsets=['upto 1hp', '2-5hp', 'above 5hp', 'other application(type here)']

model_type_Motors=['Upto 5 hp','above 5hp']
model_type_PowerTiller=['F300','FJ500']
model_type_BrushCutter=[425, 435, 450]
model_types=[model_type_Engines,model_type_Pumps,model_type_Alternators,model_type_OpenGensets,model_type_PortableGensets,model_type_SilentGensets,model_type_FuelPumpsets,model_type_ElectricPumpsets,model_type_Motors,model_type_PowerTiller,model_type_BrushCutter,[]]
#gui starting
# RMH Corporation
#my_image = tk.PhotoImage(file=r"/Users/neshaa.laksh/Downloads/Elegantthemes-Beautiful-Flat-Document.ico")
#comp_name1=tk.Label(root, image=my_image)
#comp_name1=tk.Label(root,text='   RMH' ,font='verdana 40',bg='orange')
#comp_name1.grid(row=0,column=0,sticky='ne')
comp_name2=tk.Label(root,text='RMH Corporation' ,font='verdana 40',bg='orange')
comp_name2.grid(row=0,column=1,sticky='nw')
# name
# name label
label('Name',1)
# name text box
name_textbox=tk.Entry(bd=5,width=39)
name_textbox.grid(row=1,column=1,sticky='nw',padx=10,pady=10)
# city
# city label
label('City',2)

#city textbox
city_textbox=tk.Entry(bd=5,width=39)
city_textbox.grid(row=2,column=1,sticky='nw',padx=10,pady=10)
# whatsapp phone number 
# wphn label
label('Whatsapp Number',3)
# wphn textbox
wphn_textbox=tk.Entry(bd=5,width=39)
wphn_textbox.grid(row=3,column=1,sticky='nw',padx=10,pady=10)
#product type label
label('Product type',4)
#product type drop down box
dp = ttk.Combobox(root, width=38, value=product_type)
dp.grid(row=4,column=1,sticky='nw',padx=10,pady=10)
#model type label
label('Model',5)
#model type drop down box
mt = ttk.Combobox(root, width=38)
mt.bind('<Button-1>', callback)
mt.grid(row=5,column=1,sticky='nw',padx=10,pady=10)
# c1/c2/c3 dropdown box
#label
label('Order expectation',6)
#dropdown box
co=['C1','C2','C3']
c=ttk.Combobox(root,width=38,value=co)
c.grid(row=6,column=1,sticky='nw',padx=10,pady=10)
#remarks
label('Remarks :',7)
st=tk.scrolledtext.ScrolledText(root, height=8,width=48,bd=5)
st.grid(row=7, column=1,padx=10,pady=10)
#done button
 
butt=tk.Button(root,text='Done',foreground='black',command=ExitApplication,font='verdana 12')
butt.grid(row=8,column=1,sticky='nw',padx=10,pady=10)


root.mainloop()
