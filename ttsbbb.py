# -*- coding: UTF-8 -*-

from tkinter import *
import pyttsx3

#sys.setdefaultencoding("utf-8")

root = Tk()
root.title("Pyttsx3文本转语音")
root.geometry('600x450')
root.resizable(width=True, height=True)
Label(root, text='please input text:'.encode('gbk').decode('utf8'), font=('Arial', 20)).pack()

frm = Frame(root)
scrollbar = Scrollbar(frm)
scrollbar.pack(side=RIGHT, fill=Y)
photo=PhotoImage(file="router 0.gif")
textbox = Text(frm, yscrollcommand=scrollbar.set)
textbox.pack(side=LEFT)
theLabel = Label(root, justify=RIGHT, image=photo)
theLabel.pack()
scrollbar.config(command=textbox.yview)
frm.pack()

tts = pyttsx3.init()

def readtext():
    contents=textbox.get('1.0',END)
    tts.say(contents)
    tts.runAndWait()


def textclear():
    textbox.delete(0.0, END)

Button(root, text="阅读", command = readtext, width=10, height=10, fg="white", bg="black").pack(side=RIGHT)
Button(root, text="清除", command = textclear, width=10, height=10, fg="blue", bg="orange").pack(side=LEFT)

root.mainloop()
