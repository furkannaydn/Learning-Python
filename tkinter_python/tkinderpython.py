import tkinter

window=tkinter.Tk()
window.title("Python Tkinder")
window.minsize(width=450,height=450)

def click_button():
    user_input=my_entry.get()
    print(user_input)
    
   


#label
my_label=tkinter.Label(text="this is a label",font=('Arial',"7","italic"))
#my_label.pack(side="top")#pack ekran hizlamasında kullandığımız bir fonksiyon
#my_label.place(x=0,y=10)#x y eksenine göre konumlandırdık
my_label.grid(row=0,column=0)



#button
my_button=tkinter.Button(text="this is a button",command=click_button)
#my_button.place(x=80,y=0)
my_button.grid(row=1,column=1)


#entry

my_entry=tkinter.Entry(width=20)
#my_entry.place(x=190,y=0)
my_entry.grid(row=3,column=2)









window.mainloop()