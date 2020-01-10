"""
Victor Wu
Register/Login system
"""

from tkinter import *
from tkinter import messagebox
import tkinter.messagebox
import os
import pickle

storage = {1:[],2:[],3:[]}

def delete_screen1():
    register_screen.destroy()

def delete_screen2():
    success_screen.destroy()

def delete_screen3():
    screen_wrong.destroy()

def delete_screen4():
    screen_non.destroy()
def delete_all():
    success_screen.destroy()
    login_screen.destroy()
    

def save_account():
    save_website = website_input.get()
    save_username = username_input.get()
    save_password = password_input.get()
    storage_new[1].append(save_website)
    storage_new[2].append(save_username)
    storage_new[3].append(save_password)
    pickle_out = open(username1+"dict.pickle", "wb")
    pickle.dump(storage_new, pickle_out)
    pickle_out.close()
    Label(success_screen, text = "Website:"+save_website, font = ("Times New Roman", 17)).pack()
    Label(success_screen, text = "Username:"+save_username, font = ("Times New Roman", 17)).pack()
    Label(success_screen, text = "Password:"+save_password, font = ("Times New Roman", 17)).pack()
    Label (success_screen,text = "******************************************************************************************************************************************************").pack()

    
def success():
    global storage_new
    global username_input
    global password_input
    global website_input
    storage_new = pickle.load(pickle_in)    
    username_input = StringVar()
    password_input = StringVar()
    website_input = StringVar()
    global success_screen
    success_screen = Toplevel (screen)
    success_screen.title("Success")
    success_screen.geometry("1000x900")
    Label(success_screen, text = "Welcome to PassWordSaver", font = ("Times New Roman", 20)).pack()
    Label (text = "").pack()
    Label(success_screen, text = "Please Enter Your Usernames and Their Corresponding Passwords to Securely Save Them", font = ("Times New Roman", 13)).pack()
    Label (success_screen,text = "").pack()
    Label (success_screen,text = "Website * ", width = "25", height = "2", font = ("Times New Roman", 10)).pack()
    website_entry = Entry(success_screen, textvariable = website_input)
    website_entry.pack()
    Label (success_screen,text = "Username * ", width = "25", height = "2", font = ("Times New Roman", 10)).pack()
    username_entry  = Entry(success_screen, textvariable = username_input)
    username_entry.pack()
    Label (success_screen,text = "Password * ", width = "25", height = "2", font = ("Times New Roman", 10)).pack()
    password_entry = Entry(success_screen, textvariable = password_input)
    password_entry.pack()
    Label (success_screen,text = "").pack()
    Button (success_screen,text = "Save", width = "25", height = "2", font = ("Times New Roman", 10), command = save_account).pack()
    Label (success_screen,text = "").pack()
    Button (success_screen,text = "Quit", width = "25", height = "2", font = ("Times New Roman", 10), command = delete_all).pack()
    Label (success_screen,text = "******************************************************************************************************************************************************").pack()
    if len(storage_new[1])==0:
        loop=False
    else:
        loop=True
        count1=0
        count2=0
        count3=0
        while loop:
            if count1==len(storage_new[1]):
                loop=False
            else:
                Label(success_screen, text = "Website:"+storage_new[1][count1], font = ("Times New Roman", 17)).pack()
                count1+=1
                Label(success_screen, text = "Username:"+storage_new[2][count2], font = ("Times New Roman", 17)).pack()
                count2+=1
                Label(success_screen, text = "Password:"+storage_new[3][count3], font = ("Times New Roman", 17)).pack()
                count3+=1
                Label (success_screen,text = "******************************************************************************************************************************************************").pack()


            

def wrong():
    global screen_wrong
    screen_wrong = Toplevel (screen)
    screen_wrong.title("Failure")
    screen_wrong.geometry("500x250")
    Label(screen_wrong, text = "Password Error").pack()
    Button(screen_wrong, text = "Try Again", command = delete_screen3).pack()

def user_nonexistent():
    global screen_non
    screen_non = Toplevel (screen)
    screen_non.title("Failure")
    screen_non.geometry("500x250")
    Label(screen_non, text = "User Not Found").pack()
    Button(screen_non, text = "Try Again", command = delete_screen4).pack()
    
def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info+".txt", "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close

    username_entry.delete(0, END)
    password_entry.delete(0,END)

    Label(register_screen, text = "Registration Complete!", fg = "green", font = ("Times New Roman", 10)).pack()
    Label (register_screen,text = "").pack()
    Button(register_screen, text = "OK", width = "25", height = "2", font = ("Times New Roman", 10), command = delete_screen1).pack()
    pickle_out = open(username_info+"dict.pickle", "wb")
    pickle.dump(storage, pickle_out)
    pickle_out.close()
    

def login_verify():
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)

    list_of_files = os.listdir()
    if username1+".txt" in list_of_files:
        file1 = open(username1+".txt", "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            global pickle_in
            pickle_in = open (username1+"dict.pickle", "rb")
            success()
        else:
            wrong()
    else:
        user_nonexistent()
    
def register():
    global register_screen
    register_screen = Toplevel (screen)
    register_screen.title("Registration")
    register_screen.geometry("500x400")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    Label (register_screen, text = "Please Enter Username and Password:", bg = "light grey", width = "500", height = "2", font = ("Times New Roman", 10)).pack()
    Label (register_screen,text = "").pack()
    Label (register_screen,text = "Username * ", width = "25", height = "2", font = ("Times New Roman", 10)).pack()
    username_entry  = Entry(register_screen, textvariable = username)
    username_entry.pack()
    Label (register_screen,text = "Password * ", width = "25", height = "2", font = ("Times New Roman", 10)).pack()
    password_entry = Entry(register_screen, show='*', textvariable = password)
    password_entry.pack()
    Label (register_screen,text = "").pack()
    Button (register_screen,text = "Register", width = "25", height = "2", font = ("Times New Roman", 10), command = register_user).pack()
    Label (register_screen,text = "").pack()
    
def login():
    global login_screen
    login_screen = Toplevel (screen)
    login_screen.title("Login")
    login_screen.geometry("500x250")
    global username_verify
    global password_verify
    global username_entry1
    global password_entry1
    username_verify = StringVar()
    password_verify = StringVar()
    Label (login_screen, text = "Please Enter Username and Password:", bg = "light grey", width = "500", height = "2", font = ("Times New Roman", 10)).pack()
    Label (login_screen,text = "").pack()
    Label (login_screen,text = "Username * ", width = "25", height = "2", font = ("Times New Roman", 10)).pack()
    username_entry1 = Entry(login_screen, textvariable = username_verify)
    username_entry1.pack()
    Label (login_screen,text = "Password * ", width = "25", height = "2", font = ("Times New Roman", 10)).pack()
    password_entry1 = Entry(login_screen, show='*',textvariable = password_verify)
    password_entry1.pack()
    Label (login_screen,text = "").pack()
    Button (login_screen,text = "Login", width = "25", height = "2", font = ("Times New Roman", 10), command = login_verify).pack()

def login_screen():
    global screen
    screen = Tk()
    screen.geometry ("300x150")
    screen.title ("PSWD 1.0")
    Label (text = "PSWD 1.0", bg = "light grey", width = "500", height = "2", font = ("Times New Roman", 10)).pack()
    Label (text = "").pack()
    Button (text = "Login", width = "25", height = "2", font = ("Times New Roman", 10), command = login).pack()
    Label (text = "").pack()
    Button (text = "Register", width = "25", height = "2", font = ("Times New Roman", 10), command = register).pack()
    screen.mainloop()



login_screen()
