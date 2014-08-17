import Tkinter
import tkFont
top = Tkinter.Tk()
top.geometry('250x150')
top.title("IHRD")
top.config(background='black')
window1 = Tkinter.Label(top,bg='black')
window1.pack()
def def1():
	execfile("graph.py")
button1=Tkinter.Button(top,text="District frequency",command=def1 ,bg='#981212',fg='white',font=tkFont.Font(weight='bold',family='Meera'))

button1.pack()

Tkinter.mainloop()
