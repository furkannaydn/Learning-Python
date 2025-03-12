from tkinter import *

window=Tk()
window.title("tkinder python")
window.minsize(width=600,height=600)
window.config(padx=20,pady=20)


#label
Label=Label(text="my label")
Label.config(bg="black",fg="white")
Label.config(padx=15,pady=10)
Label.pack()



#button
def button_clicked():
    print(my_text.get("1.0",END))#1-> line,0->character

button=Button(text="button",command=button_clicked)#command çalıştırılacak fonkisyonu belirler
button.config(padx=15,pady=10)
button.pack()



#entry
entry=Entry(width=20)
entry.pack()
entry.focus()#ekran açılınca ilk odaklanması gereken yeri belirtiriz



#multiline
#text
my_text=Text(width=30,height=5)
my_text.pack()



#scale
def scale_selected(value):
    print(value)

my_scale=Scale(from_=0,to=50,command=scale_selected)
my_scale.pack()


#spinbox

def spinbox_selected():
    print(my_spinbox.get())

my_spinbox=Spinbox(from_=0,to=50,width=10,command=spinbox_selected)
my_spinbox.pack()


#checkbutton
def checkbutton_selected():
    print(check_state.get())

check_state=IntVar()
my_checkbutton=Checkbutton(text="check",variable=check_state,command=checkbutton_selected)
my_checkbutton.pack()






window.mainloop()