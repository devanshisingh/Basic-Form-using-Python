import sqlite3 as s
from tkinter import *

win=Tk()
win.title('Flavium 2020')
win.geometry('500x500')

con=s.connect('Flavium2020.db')
con.execute('''CREATE TABLE STUDENT
          (SAP INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL,
           PROGRAM TEXT NOT NULL, YEAR INT(2), BRANCH TEXT NOT NULL, CRICKET TEXT,
           FOOTBALL TEXT, KABADDI TEXT, VOLLEYBALL TEXT, BADMINTON TEXT,
           CARROM TEXT);''')

def donothing():
   print("Do nothing")
   
menubar = Menu(win)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=win.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

win.config(menu=menubar)


up_pnl = Canvas(win, height=90, width=500, bg='mint cream')
up_pnl.pack()
up_pnl.create_text(250,45,fill="darkblue",font="Times 20 italic bold",
                   text="Flavium 2020")
up_pnl.create_line(170,60, 330,60, fill='darkblue', width=3)

##sb=Scrollbar(win,width=15)
##sb.pack(side = RIGHT, fill=Y)

f=Frame(win, height=400, width=500, #yscrollcommand=sb.set(0,500),
        bg='lemon chiffon')
f.pack()


sap=StringVar()
name=StringVar()
L1 = Label(f, text='Name : ', bg='lemon chiffon').place(x=10, y=25)
E1 = Entry(f, textvariable=name).place(x=75,y=25)
L2 = Label(f, text='Sap ID : ', bg='lemon chiffon').place(x=250, y=25)
E2 = Entry(f, textvariable=sap).place(x=315, y=25)

prog=StringVar()
L3 = Label(f, text='Program : ', bg='lemon chiffon').place(x=10, y=60)
R1 = Radiobutton(f,text="MBA Tech",variable=prog,value='MT',
                 bg='lemon chiffon').place(x=90, y=60)
R2 = Radiobutton(f,text="B Tech",variable=prog,value='BT',
                 bg='lemon chiffon').place(x=200, y=60)

year=IntVar()
L4 = Label(f, text='Year : ', bg='lemon chiffon').place(x=315, y=60)
y=Spinbox(f, from_=1, to=4, width=5, textvariable=year).place(x=375,y=60)

branch=StringVar()
L5 = Label(f, text='Branch : ', bg='lemon chiffon').place(x=10, y=95)
E5 = Entry(f, textvariable=branch).place(x=75, y=95)

cricket=IntVar()
football=IntVar()
kabaddi=IntVar()
vlyball=IntVar()
badminton=IntVar()
carrom=IntVar()
a="Yes"
b="No"
L6= Label(f, text='Select the game(s) : '
          , bg='lemon chiffon').place(x=10, y=150)
C1=Checkbutton(f, text="Cricket", variable=cricket, bg='lemon chiffon').place(x=150, y=150)
C2=Checkbutton(f, text="Football", variable=football, bg='lemon chiffon').place(x=250, y=150)
C3=Checkbutton(f, text="Kabaddi", variable=kabaddi, bg='lemon chiffon').place(x=350, y=150)
C4=Checkbutton(f, text="Volleyball", variable=vlyball, bg='lemon chiffon').place(x=150, y=185)
C5=Checkbutton(f, text="Badminton", variable=badminton,bg='lemon chiffon').place(x=250, y=185)
C6=Checkbutton(f, text="Carrom", variable=carrom, bg='lemon chiffon').place(x=350, y=185)


def submit():
    con.execute("INSERT INTO STUDENT VALUES (:s,:n,:p,:y,:b,:cri,:foo,:kab,:vol,:bad,:car);"
                , (sap.get(), name.get(), prog.get(), year.get(), branch.get(), cricket.get(),
                   football.get(), kabaddi.get(), vlyball.get(), badminton.get(),
                   carrom.get()))
    con.commit()
    L3 = Label(f, text='Done!', font=40, bg='lemon chiffon').place(x=125, y=300)

def clear():
    sap.set('')
    name.set('')
    prog.set('')
    year.set('')
    branch.set('')
    cricket.set(0)
    football.set(0)
    kabaddi.set(0)
    vlyball.set(0)
    badminton.set(0)
    carrom.set(0)
    
B1 = Button(f, text="Submit", command=submit).place(x=75, y=250)
B2 = Button(f, text="Clear", command=clear).place(x=250, y=250)
B3 = Button(f, text="Quit", command=quit).place(x=400, y=250)


win.mainloop()
