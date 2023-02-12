from tkinter import *

window=Tk()
window.geometry("345x370")
window.title("Calculator")
window.resizable(False,False)
window.configure(bg="#17161b")

equation=""
def show(value):
    global equation
    equation+=value
    label_result.configure(text=equation)

def calculate():
    global equation
    result=""
    if equation  !="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    label_result.configure(text=result)

def backspace():
    global equation
    equation=equation[:-1]
    label_result.configure(text=equation)

def clear():
    global equation
    equation=""
    label_result.configure(text=equation)





label_result=Label(window, width=25, height=2, text="", font=("arial",30))
label_result.pack()

Button(window, text=".", width=6, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show(".")).place(x=5,y=100)
Button(window, text="/", width=6, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("/")).place(x=90,y=100)
Button(window, text="%", width=6, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("%")).place(x=175,y=100)
Button(window, text="*", width=6, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("*")).place(x=260,y=100)

Button(window, text="7", width=6, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("7")).place(x=5,y=150)
Button(window, text="8", width=6, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("8")).place(x=90,y=150)
Button(window, text="9", width=6, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("9")).place(x=175,y=150)
Button(window, text="-", width=6, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("-")).place(x=260,y=150)

Button(window, text="4", width=6, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("4")).place(x=5,y=200)
Button(window, text="5", width=6, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("5")).place(x=90,y=200)
Button(window, text="6", width=6, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("6")).place(x=175,y=200)
Button(window, text="+", width=6, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("+")).place(x=260,y=200)

Button(window, text="1", width=6, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("1")).place(x=5,y=250)
Button(window, text="2", width=6, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("2")).place(x=90,y=250)
Button(window, text="3", width=6, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("3")).place(x=175,y=250)
Button(window, text="=", width=6, height=4, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#fe9037",command=lambda: calculate()).place(x=260,y=250)

Button(window, text="0", width=6, height=2, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("0")).place(x=5,y=300)
Button(window, text="C", width=6, height=2, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: backspace()).place(x=90,y=300)
Button(window, text="AC", width=6, height=2, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: clear()).place(x=175,y=300)




window.mainloop()
