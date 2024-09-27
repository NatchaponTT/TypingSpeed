from operator import index
import sqlite3
from tkinter import *
import random
from tkinter import messagebox
from tkinter.tix import LabelEntry
from words import *

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
    menubar.add_command(label="Game",command=playgame)
    menubar.add_command(label="score",command=showscore)
    menubar.add_command(label="Ranking",command=ranking)
    menubar.add_command(label="Logout", command=logoutClick)
    menubar.add_command(label="Exit", command=root.quit)
    return root

def loginlayout(): #เปลี่ยนรูป
    global userentry,  pwdentry,  loginframe
    
    loginframe = Frame(root, bg='#709fb0')
    loginframe.rowconfigure((0, 1, 2, 3), weight=1)
    loginframe.columnconfigure((0, 1), weight=1)
    root.title("Login")
    emptyMenu = Menu(root) 
    root.config(bg='lightblue', menu=emptyMenu)   
    
    Label(loginframe, text="Speed Typing App", font="Calibri 26 bold", image=img1, compound=LEFT, bg='#709fb0', fg='#e4fbff').grid(row=0, columnspan=2)
    Label(loginframe, text="User name : ", bg='#709fb0', fg='#e4fbff', padx=20).grid(row=1, column=0, sticky='e')
    userentry = Entry(loginframe, bg='#e4fbff', width=20)
    userentry.grid(row=1, column=1, sticky='w', padx=20)
    pwdentry = Entry(loginframe, bg='#e4fbff', width=20, show='*')
    pwdentry.grid(row=2, column=1, sticky='w', padx=20)
    Label(loginframe, text="Password  : ", bg='#709fb0', fg='#e4fbff', padx=20).grid(row=2, column=0, sticky='e')
    Button(loginframe, text="Register", width=10, command=regiswindow).grid(row=3, column=0, pady=20, ipady=15, sticky='w', padx=20)
    Button(loginframe, text="Login", width=10, command=loginclick).grid(row=3, column=1, pady=20, ipady=15, sticky='e', padx=20)
    
    #grid Frame to root
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
    
    Label(regisframe, text="Registration Form", font="Calibri 26 bold", fg='#e4fbff', image=img1, compound=LEFT, bg='#1687a7').grid(row=0, column=0, columnspan=2, sticky='news', pady=10)
    Label(regisframe, text='First name : ', bg='#8ac4d0', fg='#f6f5f5').grid(row=1, column=0, sticky='e', padx=10)
    firstname = Entry(regisframe, width=20, bg='#d3e0ea', textvariable=fname)
    firstname.grid(row=1, column=1, sticky='w', padx=10)
    Label(regisframe, text='Last name : ', bg='#8ac4d0', fg='#f6f5f5').grid(row=2, column=0, sticky='e', padx=10)
    lastname = Entry(regisframe, width=20, bg='#d3e0ea', textvariable=lname)
    lastname.grid(row=2, column=1, sticky='w', padx=10)
    Label(regisframe, text="Username : ", bg='#8ac4d0', fg='#f6f5f5').grid(row=3, column=0, sticky='e', padx=10)
    newuser = Entry(regisframe, width=20, bg='#d3e0ea', textvariable=newuserinfo)
    newuser.grid(row=3, column=1, sticky='w', padx=10)
    Label(regisframe, text="Password : ", bg='#8ac4d0', fg='#f6f5f5').grid(row=4, column=0, sticky='e', padx=10)
    newpwd = Entry(regisframe, width=20, bg='#a1cae2', textvariable=newpwdinfo, show='*')
    newpwd.grid(row=4, column=1, sticky='w', padx=10)
    Label(regisframe, text="Confirm Password : ", bg='#8ac4d0', fg='#f6f5f5').grid(row=5, column=0, sticky='e', padx=10)
    cfpwd = Entry(regisframe, width=20, bg='#a1cae2', textvariable=cfinfo, show='*')
    cfpwd.grid(row=5, column=1, sticky='w', padx=10)
    
    
    Label(regisframe, text="Gender : ", bg='#8ac4d0', fg='#f6f5f5').grid(row=6, column=0, sticky='e', padx=10)
    Radiobutton(regisframe, text='Male', bg='#8ac4d0', fg='#000', variable=genderinfo, value='Male').grid(row=6, column=1, sticky='w')
    Radiobutton(regisframe, text='Female', bg='#8ac4d0', fg='black', variable=genderinfo, value='Female').grid(row=7, column=1, sticky='w')
    genderinfo.set('Male')
    #Add Cancel button | row=8
    regisaction = Button(regisframe, text="Register Submit", command=registration)
    regisaction.grid(row=8, column=1, ipady=5, ipadx=5, pady=5, sticky='w')
    Button(regisframe, text="Cancel", command=exitRegistClick).grid(row=8, column=1, ipady=5, ipadx=5, pady=5, sticky='e')
    
    regisframe.grid(row=1, column=1, columnspan=2, rowspan=2, sticky='news')
    
    firstname.focus_force()

def profilewindow() : #เปลี่ยนรูป 
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

    if profile_data :
        Label(profile_frm,image=img1,bg="skyblue").grid(row=0, columnspan=4, pady=30)
        
        Label(profile_frm, text='Welcome to Speed Typing Game  ', bg='skyblue', fg='white', padx=5).grid(row= 1, column=0, sticky='news', columnspan=2)
        Label(profile_frm, text=profile_data[0] + ' ' + profile_data[1], bg='skyblue', fg='white', padx=5).grid(row= 2, column=0, sticky='news', columnspan=2)

        
    Button(profile_frm, text="Logout", command=logoutClick).grid(row=3, column=1)
    
    profile_frm.place(x=0, y=0, width=w, height=h)


def playgame(): # ทำให้รับคะแนนได้
    import index
    

def showscore(): # บอกชื่อ,คะแนนล่าสุด,รูปว่าเป็นผชผญ
    print()

def ranking(): # เอาคะแนนเปลี่ยนเป็นแรงค์ แล้วทำตาราง
    print()

def logoutClick():
    profile_frm.destroy()
    loginlayout() 

def loginclick() :   
    global user
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
                    #update_page(result[2], result[3])   #call update_page and pass firstname and lastname via parameter
                else :
                    messagebox.showwarning("Admin:", "Incorrect Password")
                    pwdentry.select_range(0, END)
                    pwdentry.focus_force()
        else :
            messagebox.showerror("Admin:", "Username not found\n Please register before Login")
            userentry.focus_force()

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
        #Check exist username
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
                cursor.execute(sql_ins,  [_username,  _password,  _fname,  _lname,  _gender])
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


w = 1000 
h = 600



createconnection()
root = mainwindow()

img1 = PhotoImage(file='images\profile_f.png').subsample(5,5)


sql_cnt = 'SELECT count(*) FROM student'
cursor.execute(sql_cnt)
cnt_stu = cursor.fetchone()
student_cnt = cnt_stu[0] + 1

student_cnt_lb = StringVar()
student_id = StringVar()
student_name = StringVar()
student_list = []


fname = StringVar()
lname = StringVar()
newuserinfo = StringVar()
newpwdinfo = StringVar()
cfinfo = StringVar()
genderinfo = StringVar()
radiospy =IntVar()
loginlayout()

root.mainloop()
cursor.close() 
conn.close() 