
import tkinter as tk

root= tk.Tk()
root.geometry("600x400")

root.title("My To-Do List")
def add_command():
    task=ent.get()
    lbox.insert(tk.END,task)
    ent.delete(0,tk.END)

def mark_command():
    pos=lbox.curselection()[0]
    text=lbox.get(pos)
    lbox.delete(pos)
    lbox.insert(tk.END,f"{text}\u2713")
    
def del_command():
    pos=lbox.curselection ()[0]
    
    lbox.delete(pos)
    
        
    

lb1=tk.Label(root, text="Enter task:",font=('calibri',15))
lb1.place(x=10,y=15)

ent=tk.Entry(root,width=50)
ent.place(x=120,y=20)
lbox=tk.Listbox(root,width=50,height=10)
lbox.place(x=120,y=70)
btn1=tk.Button(root,text='ADD' ,font=('calibri,15'),width=12,command=add_command)
btn1.place(x=20,y=250)
btn2=tk.Button(root,text='MARK' ,font=('calibri,15'),width=12,command=mark_command)
btn2.place(x=210,y=250)
btn3=tk.Button(root,text='REMOVE' ,font=('calibri,15'),width=15,command=del_command)
btn3.place(x=400,y=250)

root.mainloop()
