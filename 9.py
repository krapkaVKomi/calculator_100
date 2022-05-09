from tkinter import Message
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import math

''' ФУНКЦІЇ КНОПОК  '''



def eight():
    try:
        n = int(message_entry.get()) 
        b = int(8)
        r = ''
        while n > 0:
            r = str(n % 8) + r
            n //= b
        messagebox.showinfo("вісімкова", str(r))

    except ValueError:
        ve = 'Не коректно введені данні'
        messagebox.showerror("ValueError", str(ve))

def ten():
    try:
        n = int(message_entry.get()) 
        s = ''
        h = '0123456789ABCDEF'
        while n > 0:
            s = h[n % 16] + s
            n = n // 16
        messagebox.showinfo("шіснадцяткова", str(s))
       
    except ValueError:
        ve = 'Не коректно введені данні'
        messagebox.showerror("ValueError", str(ve))




def two():
    try:
        a=int(message_entry.get())             # вводимо число
        c=[]                             # створюємо порожній список для запису цифр числа у двійковій системі числення
        while a!=0:                # поки дане число ще можна ділити
            b=a%2                       # знаходимо остачу
            c.append(b)              # записуємо остачу в список
            a=a//2                        # знаходимо частку від ділення
        c=c[::-1]                      # перепишемо у списку цифри числа у зворотньому порядку
        messagebox.showinfo("двійкова", str(c))
    except ValueError:
        ve = 'Не коректно введені данні'
        messagebox.showerror("ValueError", str(ve))

def sin_funk():
    try:
        info = math.sin(float(message_entry.get()))
        messagebox.showinfo("sin(A) в радіанах ", str(info))
    except ValueError:
        ve = 'Не коректно введені данні'
        messagebox.showerror("ValueError", str(ve))

def cos_funk():
    try:
        info = math.cos(float(message_entry.get()))
        messagebox.showinfo("cos(A) в радіанах", str(info))
    except ValueError:
        ve = 'Не коректно введені данні'
        messagebox.showerror("ValueError", str(ve))

def tg_funk():
    try:
        info = math.tan(float(message_entry.get()))
        messagebox.showinfo("tg(A) в радіанах", str(info))
    except ValueError:
        ve = 'Не коректно введені данні'
        messagebox.showerror("ValueError", str(ve))

def ctg_funk():
    try:
        info = math.cos(float(message_entry.get())) / math.sin(float(message_entry.get()))
        messagebox.showinfo("ctg(A) в радіанах", str(info))
    except ValueError:
        ve = 'Не коректно введені данні'
        messagebox.showerror("ValueError", str(ve))




def plus():
    try:
        info = float(message_entry.get()) + float(message_entry2.get())
        messagebox.showinfo("+", str(info))
    except ValueError:
        ve = 'Не коректно введені данні'
        messagebox.showerror("ValueError", str(ve))


def minus():
    try:
        info = float(message_entry.get()) - float(message_entry2.get())
        messagebox.showinfo("-", str(info))
    except ValueError:
        ve = 'Не коректно введені данні'
        messagebox.showerror("ValueError", str(ve))


def p2():
    try:
        info = float(message_entry.get()) * float(message_entry2.get())
        messagebox.showinfo("*", str(info))
    except ValueError:
        ve = 'Не коректно введені данні'
        messagebox.showerror("ValueError", str(ve))


def m2():
    try:
        if float(message_entry2.get()) == 0:
            ve = 'На нуль ділити не можна'
            messagebox.showerror("ZeroDivisionError", str(ve))
        else:
            info = float(message_entry.get()) / float(message_entry2.get())
            messagebox.showinfo("/", str(info))
    except ValueError:
        ve = 'Не коректно введені данні'
        messagebox.showerror("ValueError", str(ve))


def p3():
    try:
        info = float(message_entry.get()) ** float(message_entry2.get())
        messagebox.showinfo("**", str(info))
    except ValueError:
        ve = 'Не коректно введені данні'
        messagebox.showerror("ValueError", str(ve))


def delete1_funk():
    message_entry.delete(-1)

def delete2_funk():
    message_entry2.delete(-1)

def delete_funk():
    message_entry2.delete(0, END)
    message_entry.delete(0, END)




"""  РОЗМІТКА ВІКНА """
root = Tk()
root.title("round to 100")
root.geometry("260x260")
root.resizable(height = False, width = False)

label = tk.Label(text="Калькулятор")
label.pack(fill=tk.X)
message_entry = Entry(root, width = 20)
message_entry.pack(fill=tk.X)


delete1 = Button(text="очищення верхнього рядка (рядка А)   <--", command=delete1_funk)
delete1.pack(fill=tk.X)

delete_all = Button(text="очистити обидва рядки   (С)", command=delete_funk)
delete_all.pack(fill=tk.X)

delete2 = Button(text="очищення нижнього рядка (рядка В)   <--", command=delete2_funk)
delete2.pack(fill=tk.X)


message_entry2 = Entry(root, width = 20)
message_entry2.pack(fill=tk.X)


plus_button = Button(text="  +  ", command=plus)
plus_button.place(x=1, y=140)

minus_button = Button(text="  -  ", command=minus)
minus_button.place(x=31, y=140)

plus_button = Button(text="  *  ", command=p2)
plus_button.place(x=61, y=140)

minus_button = Button(text="  /  ", command=m2)
minus_button.place(x=91, y=140)

plus_button = Button(text=" ** ", command=p3)
plus_button.place(x=121, y=140)

sin_button = Button(text=" sin(A) ", command=sin_funk)
sin_button.place(x=153, y=140)

sin_button = Button(text=" cos(A)  ", command=cos_funk)
sin_button.place(x=203, y=140)

sin_button = Button(text="   tg(A) ", command=tg_funk)
sin_button.place(x=1, y=170)

sin_button = Button(text=" ctg(A) ", command=ctg_funk)
sin_button.place(x=1, y=200)

sin_button = Button(text="(А) від десяткової до двійкової          ", command=two)
sin_button.place(x=51, y=170)

sin_button = Button(text="(А) від десяткової до шіснацяткової", command=ten)
sin_button.place(x=51, y=200)

sin_button = Button(text="(А) від десяткової до вісімкової        ", command=eight)
sin_button.place(x=51, y=230)


label_documentation = tk.Label(text=" : )")
label_documentation.place(x=1, y=230)


















root.mainloop()