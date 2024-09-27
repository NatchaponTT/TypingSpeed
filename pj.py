from asyncio import streams
from ctypes.wintypes import PLARGE_INTEGER
from operator import index
import sqlite3
from tkinter import *
import random
from tkinter import messagebox
from tkinter.tix import LabelEntry
from words import *
from tkinter import ttk

def createconnection() :
    global conn, cursor
    conn = sqlite3.connect('1640705495.db')
    cursor = conn.cursor()

def mainwindow() :
    global menubar
    root = Tk()
    x = root.winfo_screenwidth()/2 - w/2
    y = root.winfo_screenheight()/2 - h/2
    root.geometry("%dx%d+%d+%d"%(w, h, x, y))
    root.config(bg='#28527a')
    root.title("My Application: ")
    root.option_add('*font', "Calibri 24 bold")
    root.rowconfigure((0, 1, 2, 3), weight=1)
    root.columnconfigure((0, 1, 2, 3), weight=1)
    menubar = Menu(root)
    menubar.add_command(label="Game",command=game)
    menubar.add_command(label="Score",command=showscore)
    menubar.add_command(label="Ranking",command=ranking)
    menubar.add_command(label="Exit", command=root.quit)
    return root

def loginlayout(): 
    global userentry,  pwdentry,  loginframe
    
    loginframe = Frame(root, bg='#709fb0')
    loginframe.rowconfigure((0, 1, 2, 3), weight=1)
    loginframe.columnconfigure((0, 1), weight=1)
    root.title("Login")
    emptyMenu = Menu(root) 
    root.config(bg='lightblue', menu=emptyMenu)
    
    Label(loginframe, text=" Speed Typing App", font="Calibri 26 bold", image=img_key, compound=LEFT, bg='#709fb0', fg='#FFFFFF').grid(row=0, columnspan=2)
    Label(loginframe, text="User name : ", bg='#709fb0', fg='#FFFFFF', padx=20).grid(row=1, column=0, sticky='e')
    userentry = Entry(loginframe, bg='#FFFFFF',width=20)
    userentry.grid(row=1, column=1, sticky='w', padx=20)
    pwdentry = Entry(loginframe, bg='#FFFFFF', width=20, show='*')
    pwdentry.grid(row=2, column=1, sticky='w', padx=20)
    Label(loginframe, text="Password  : ", bg='#709fb0', fg='#FFFFFF', padx=20).grid(row=2, column=0, sticky='e')

    Button(loginframe, image=img_re, activebackground='#709fb0',bg='#709fb0', bd=0, command=regiswindow).grid(row=3, column=0, pady=20, ipady=15, sticky='w', padx=20)
    Button(loginframe, image=img_log, activebackground='#709fb0',bg='#709fb0', bd=0,command=loginclick).grid(row=3, column=1, pady=20, ipady=15, sticky='e', padx=20)
    
    
    loginframe.grid(row=1, column=1, columnspan=2, rowspan=2, sticky='news')

def regiswindow():
    global firstname, lastname, newuser, newpwd, cfpwd 
    global regisframe
    loginframe.destroy()
    
    root.title("Welcome to User Registration : ")
    root.config(bg='lightblue')    
    regisframe = Frame(root, bg='#8ac4d0')
    regisframe.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
    regisframe.columnconfigure((0, 1), weight=1)
    
    Label(regisframe, text=" Registration Form", font="Calibri 26 bold", fg='#FFFFFF', image=img_key, compound=LEFT, bg='#1687a7').grid(row=0, column=0, columnspan=2, sticky='news', pady=10)
    Label(regisframe, text='First name : ', bg='#8ac4d0', fg='#FFFFFF').grid(row=1, column=0, sticky='e', padx=10)
    firstname = Entry(regisframe, width=20, bg='#FFFFFF', textvariable=fname)
    firstname.grid(row=1, column=1, sticky='w', padx=10)
    Label(regisframe, text='Last name : ', bg='#8ac4d0', fg='#FFFFFF').grid(row=2, column=0, sticky='e', padx=10)
    lastname = Entry(regisframe, width=20, bg='#FFFFFF', textvariable=lname)
    lastname.grid(row=2, column=1, sticky='w', padx=10)
    Label(regisframe, text="Username : ", bg='#8ac4d0', fg='#FFFFFF').grid(row=3, column=0, sticky='e', padx=10)
    newuser = Entry(regisframe, width=20, bg='#d3e0ea', textvariable=newuserinfo)
    newuser.grid(row=3, column=1, sticky='w', padx=10)
    Label(regisframe, text="Password : ", bg='#8ac4d0', fg='#FFFFFF').grid(row=4, column=0, sticky='e', padx=10)
    newpwd = Entry(regisframe, width=20, bg='#a1cae2', textvariable=newpwdinfo, show='*')
    newpwd.grid(row=4, column=1, sticky='w', padx=10)
    Label(regisframe, text="Confirm Password : ", bg='#8ac4d0', fg='#FFFFFF').grid(row=5, column=0, sticky='e', padx=10)
    cfpwd = Entry(regisframe, width=20, bg='#a1cae2', textvariable=cfinfo, show='*')
    cfpwd.grid(row=5, column=1, sticky='w', padx=10)
    
    
    Label(regisframe, text="Gender : ", bg='#8ac4d0', fg='#FFFFFF').grid(row=6, column=0, sticky='e', padx=10)
    Radiobutton(regisframe, text='Male', bg='#8ac4d0', fg='#000', variable=genderinfo, value='Male').grid(row=6, column=1, sticky='w')
    Radiobutton(regisframe, text='Female', bg='#8ac4d0', fg='black', variable=genderinfo, value='Female').grid(row=7, column=1, sticky='w')
    genderinfo.set('Male')
    #Add Cancel button | row=8
    regisaction = Button(regisframe,image=img_resm, activebackground='#8ac4d0',bg='#8ac4d0', bd=0, command=registration)
    regisaction.grid(row=8, column=1, ipady=5, ipadx=5, pady=5, sticky='w')
    Button(regisframe,image=img_can, activebackground='#8ac4d0',bg='#8ac4d0', bd=0, command=exitRegistClick).grid(row=8, column=1, ipady=5, ipadx=5, pady=5, sticky='e')
    
    regisframe.grid(row=1, column=1, columnspan=2, rowspan=2, sticky='news')
    
    firstname.focus_force()

def profilewindow() : 
    global profile_frm, profile_data  
    user = userentry.get()
    loginframe.destroy()
    
    root.title("Welcome : "+user)
    root.config(bg='lightblue', menu=menubar) 
    profile_frm = Frame(root,  bg='skyblue')
    profile_frm.rowconfigure((0, 1, 2, 3), weight=1)
    profile_frm.columnconfigure((0, 1), weight=1)
    
    sql_user = "SELECT fname,lname,gender FROM login WHERE user=?"
    cursor.execute(sql_user,[user])
    profile_data = cursor.fetchone()

    
    if result[4] == 'Male':
        Label(profile_frm, image=img_m, bg="skyblue").grid(row=0 ,columnspan=4,pady=30)
    else:
        Label(profile_frm, image=img_f, bg="skyblue").grid(row=0 ,columnspan=4,pady=30)
        
    Label(profile_frm, text='Welcome to Speed Typing Game  ', bg='skyblue', fg='white', padx=5).grid(row= 1, column=0, sticky='news', columnspan=2)
    Label(profile_frm, text=profile_data[0] + ' ' + profile_data[1], bg='skyblue', fg='white', padx=5).grid(row= 2, column=0, sticky='news', columnspan=2)

        
    Button(profile_frm,image=img_out, activebackground='#709fb0',bg='skyblue', bd=0, command=logoutClick).grid(row=3, column=1)
    
    profile_frm.place(x=0, y=0, width=w, height=h)

def game():
    global fontlabel,startlabel,wordlabel,scorelabel,scorelabelcount,timerlabel,timerlabelcount,gameinstruction,wordentry,miss,count,sliderwords,timer,score
    root= Tk()
    root.geometry('800x600+400+100')
    root.title('Speed Typing App')


    score=0
    miss=0
    timer=60
    count=0
    sliderwords=''


    fontlabel=Label(root,text='',font=('airal',25,'italic bold'),fg='purple',width=40)
    fontlabel.place(x=10,y=10)

    slider()

    startlabel=Label(root,text='Start Typing',font=('airal',30,'italic bold'),bg='black',fg='white')
    startlabel.place(x=275,y=50)

    random.shuffle(words)

    wordlabel=Label(root,text=words[0],font=('airal',45,'italic bold'),fg='green')
    wordlabel.place(x=350,y=240)


    scorelabel=Label(root,text='Your Score:',font=('arial',25,'italic bold'),fg='red')
    scorelabel.place(x=10,y=100)

    scorelabelcount=Label(root,text=score,font=('arial',25,'italic bold'),fg='blue')
    scorelabelcount.place(x=150,y=180)

    timerlabel=Label(root,text='Time Left:',font=('arial',25,'italic bold'),fg='red')
    timerlabel.place(x=600,y=100)

    timerlabelcount=Label(root,text=timer,font=('arial',25,'italic bold'),fg='blue')
    timerlabelcount.place(x=600,y=180)



    gameinstruction= Label(root,text='Type the Word and hit enter button',font=('arial',25,'italic bold'),fg='grey')
    gameinstruction.place(x=150,y=500)



    wordentry= Entry(root,font=('airal',25,'italic bold'),bd=10,justify='center')
    wordentry.place(x=250,y=330)
    wordentry.focus_set()



    root.bind('<Return>',startgame)
    
def startgame(event):
    global score, miss
    if timer==60:
        time()
    gameinstruction.configure(text='')
    startlabel.configure(text='')
    if wordentry.get()== wordlabel['text']:
        score +=1
        scorelabelcount.configure(text=score)
    else:
        miss +=1
    random.shuffle(words)
    wordlabel.configure(text=words[0])
    wordentry.delete(0,END)    

def ranking() :
    global mytree,rank_f

    rank_f = Frame(root,bg='lightblue')
    rank_f.place(x=0, y=0, width=w, height=h)
    rank_f.columnconfigure((0, 1), weight=1)
    rank_f.rowconfigure((0, 1, 2, 3), weight=1)
    Label(rank_f,text="Player List").grid(row=0,columnspan=4,sticky='news')

    mytree = ttk.Treeview(rank_f, columns=('col1','col2','col3',))
    mytree.grid(row=2, column=0, columnspan=2,sticky='news')
    #create headings
    mytree.heading('col1', text='User')
    mytree.heading('col2', text='Score', anchor=CENTER)
    mytree.heading('col3', text='Rank', anchor=CENTER)
    #format columns
    mytree.column('col1',anchor=CENTER, width=250)
    mytree.column('col2',anchor=CENTER, width=250)
    mytree.column('col3',anchor=CENTER, width=150)
    mytree.column('#0',width=0,minwidth=0) #default column
    fetchTree()
    Button(rank_f,image=img_can, activebackground='#8ac4d0',bg='lightblue', bd=0, command=exitrankClick).grid(row=3, column=0, columnspan=2)

def exitrankClick():
    rank_f.destroy()
    profilewindow()
    
def logoutClick():
    profile_frm.destroy()
    loginlayout() 

def loginclick() :   
    global user, result
    user = userentry.get()
    pwd = pwdentry.get()
    
    if user == "" :
        messagebox.showwarning("Admin:", "Please enter username")
        userentry.focus_force()
    else :
        sql = "SELECT * FROM login WHERE user=?"
        cursor.execute(sql, [user])
        result = cursor.fetchall()
        if result :
            if pwd == "" :
                messagebox.showwarning("Admin:", "Please enter password")
                pwdentry.focus_force()
            else :
                sql = "SELECT * FROM login WHERE user=? and pwd=? "
                cursor.execute(sql, [user, pwd])
                result = cursor.fetchone()
                if result :
                    messagebox.showinfo("Admin:", "Login Successfully")
                    profilewindow()
                else :
                    messagebox.showwarning("Admin:", "Incorrect Password")
                    pwdentry.select_range(0, END)
                    pwdentry.focus_force()
        else :
            messagebox.showerror("Admin:", "Username not found\n Please register before Login")
            userentry.focus_force()

def slider():
    global count,sliderwords
    text='Speed Typing App'
    if count>= len(text):
        count =0
        sliderwords =''
    sliderwords += text[count]
    count +=1
    fontlabel.configure(text=sliderwords)
    fontlabel.after(150,slider)

def time():
    global timer,score,miss
    if timer>11:
        pass
    else:
        timerlabelcount.configure(fg='red')
    if timer>0:
        timer -=1
        timerlabelcount.configure(text=timer)
        timerlabelcount.after(1000,time)
    else:
        total = score-miss
        gameinstruction.configure(text='Hit = {} | Miss = {} | Total Score = {}'.format(score,miss,total))
        rr= messagebox.askretrycancel('Notification','Wanna Play Again!!!!')
        if rr==True:
            score=0
            miss=0
            timer=60
            timerlabelcount.configure(text=timer)
            wordlabel.configure(text=words[0])
            scorelabelcount.configure(text=score)
            wordentry.delete(0, END)
        else :
            sql = 'UPDATE player SET score = ? WHERE user = ?'
            cursor.execute(sql,(score,result[0]))
            conn.commit()
            #คำนวน rank แล้ว อัพ ใน db
            sumscore()
        
def showscore(): 
    global score_frm
    profile_frm.destroy()
    root.title("Score")
    root.config(bg='lightblue') 
    score_frm = Frame(root,  bg='skyblue')
    score_frm.rowconfigure((0, 1, 2, 3), weight=1)
    score_frm.columnconfigure((0, 1), weight=1)

    sql_py = "SELECT score,rank FROM player WHERE user=?"
    cursor.execute(sql_py,[user])
    profile_py = cursor.fetchone()

    if profile_py[1] == "Bronze":
        Label(score_frm,image=img_b,bg='skyblue').grid(row=0,column=0,columnspan=2,sticky='news')
    if profile_py[1] == "Silver":
        Label(score_frm,image=img_sil,bg='skyblue').grid(row=0,column=0,columnspan=2,sticky='news')
    if profile_py[1] == "Gold":
        Label(score_frm,image=img_gold,bg='skyblue').grid(row=0,column=0,columnspan=2,sticky='news')
    if profile_py[1] == "Platinum":
        Label(score_frm,image=img_plat,bg='skyblue').grid(row=0,column=0,columnspan=2,sticky='news')

    Label(score_frm,text='Name : '+profile_data[0] + ' ' + profile_data[1], bg='skyblue', fg='white', padx=5).grid(row=1, column=0, sticky='news', columnspan=2)
    Label(score_frm,text='Score : %d'%profile_py[0], bg='skyblue', fg='white', padx=5).grid(row=2, column=0, sticky='news', columnspan=2)

    score_frm.place(x=0, y=0, width=w, height=h)

def registration() :
    _fname = fname.get()
    _lname = lname.get()
    _username = newuserinfo.get()
    _password = newpwdinfo.get()
    _cfpass = cfinfo.get()
    _gender = genderinfo.get()
    
    if _fname == "":
        messagebox.showwarning("Admin",  'Please enter firstname')
        firstname.focus_force()
    elif _lname == "":
        messagebox.showwarning("Admin",  'Please enter lastname')
        lastname.focus_force()  
    elif _username == "":
        messagebox.showwarning("Admin",  'Please enter username')
        newuser.focus_force()
    elif _password == "":
        messagebox.showwarning("Admin",  'Please enter password')
        newpwd.focus_force()
    elif _cfpass == "":
        messagebox.showwarning("Admin",  'Please enter confirm password')
        cfpwd.focus_force()
    else:
        sql_chk = "SELECT * FROM login WHERE user=?"
        cursor.execute(sql_chk,  [_username])  
        chk_result = cursor.fetchall()
        if chk_result:
            messagebox.showwarning("Admin",  'Username is already exists')
            newuser.focus_force()
            newuser.select_range(0, END)
        else:
            if _password == _cfpass:
                sql_ins = 'INSERT INTO login VALUES (?, ?, ?, ?, ?)'
                cursor.execute(sql_ins, [_username,  _password,  _fname,  _lname,  _gender])
                sql_ins = 'INSERT INTO player VALUES (?, ?, ?)'
                cursor.execute(sql_ins, [_username,  "0",  "none",])
                conn.commit()
                retrivedata()
                messagebox.showinfo("Admin", "Registration Successfully")
                firstname.delete(0, END)
                lastname.delete(0, END)
                newuser.delete(0, END)
                newpwd.delete(0, END)
                cfpwd.delete(0, END)
                exitRegistClick()
            else:
                messagebox.showwarning("Admin",  'Confirm password is not matched')

def retrivedata():
    sql = "SELECT * FROM login"
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Total row = ", len(result))
    for i, data in enumerate(result) :
        print("Row#", i+1, data)

def exitRegistClick():
    regisframe.destroy()
    loginlayout() 

def sumscore():  
    if score > 0  :
      if score > 70 :
        rank = "Platinum"
      elif score > 50 and score < 69 :
        rank = "Gold"
      elif score > 21 and score < 49 :
        rank = "Silver"
      elif score > 0 and score < 20 :
        rank = "Bronze"
    
    print(user)
    print(score)
    print(rank)

    sql_ins_stu =''' UPDATE player 
                     SET user=? ,score=? ,rank=?
                     WHERE user=? '''

    cursor.execute(sql_ins_stu,[user,score,rank,user])
    conn.commit()

def fetchTree():
    mytree.delete(*mytree.get_children()) # clear Treeview
    sql = 'SELECT * FROM player'
    cursor.execute(sql)
    result = cursor.fetchall()
    if result:
      for i, data in enumerate(result):
        mytree.insert("","end",values=(data[0],data[1],data[2]))
        print(data)

w = 1000
h = 600


createconnection()
root = mainwindow()

img_f = PhotoImage(file='images\profile_f.png').subsample(5,5)
img_m = PhotoImage(file='images\profile_m.png')
img_key = PhotoImage(file='images\key3.png').subsample(2,2)
img_log = PhotoImage(file='images\login.png')
img_re = PhotoImage(file='images/register.png')
img_out = PhotoImage(file='images/logout.png').subsample(2,2)
img_resm = PhotoImage(file='images/registersm.png').subsample(2,2)
img_can = PhotoImage(file='images\Cancel.png').subsample(2,2)
img_b = PhotoImage(file='images/bronze.png')
img_sil = PhotoImage(file='images\silver2.png')
img_gold = PhotoImage(file='images\goldiii.png')
img_plat = PhotoImage(file='images\platinum2.png')



student_cnt_lb = StringVar()
student_id = StringVar()
student_name = StringVar()
player_list = ['user','score','rank']

user = StringVar()
score = StringVar()
rank = StringVar()
spy = [DoubleVar() for i in player_list]

fname = StringVar()
lname = StringVar()
newuserinfo = StringVar()
newpwdinfo = StringVar()
cfinfo = StringVar()
genderinfo = StringVar()
radiospy =IntVar()

loginlayout()

root.resizable(False,False)
root.mainloop()
cursor.close() 
conn.close() 