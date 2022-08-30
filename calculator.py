#Calculator with GUI (Hossein Razghandi)
from tkinter import *
from tkinter import messagebox
from tkinter.font import *

#insert the buttons values to entry
def insert_to_entry(num):
    entry.insert(END, num)


#clear the entry 
def clear_entry():
    entry.delete(0, END)


#try to show the result of entry in a messagebox
def show_result():
    try:
        result = eval(entry.get())
        messagebox.showinfo('Result', f"{result}")
        clear_entry()
    except:
        messagebox.showerror('Error', "Invalid input!!")
        
#GUI of the calculator that shows the buttons and entry
window = Tk()

my_font = Font(family='Helvatica' , size=20)
my_font_2 = Font(family='Consolas' , size=25)

window.geometry("430x370")
window.title("Calculator")

window['bg'] = '#ffcccb'

entry = Entry(window, font= my_font)
entry.grid(row=0, column=0, columnspan=5, ipady=10, padx=35, pady=17, sticky=W+E)

button_1 = Button(window, text='1', font=my_font_2, width=2, height=1, \
                    command=lambda: insert_to_entry('1'))
button_1.grid(row=1, column=0, padx=2, pady=2)

button_2 = Button(window, text='2', font=my_font_2, width=2, height=1, \
                    command=lambda: insert_to_entry('2'))
button_2.grid(row=1, column=1, padx=2, pady=2)

button_3 = Button(window, text='3', font=my_font_2, width=2, height=1, \
                    command=lambda: insert_to_entry('3'))
button_3.grid(row=1, column=2, padx=2, pady=2)

button_4 = Button(window, text='4', font=my_font_2, width=2, height=1, \
                    command=lambda: insert_to_entry('4'))
button_4.grid(row=2, column=0, padx=2, pady=2)

button_5 = Button(window, text='5', font=my_font_2, width=2, height=1, \
                    command=lambda: insert_to_entry('5'))
button_5.grid(row=2, column=1, padx=2, pady=2)

button_6 = Button(window, text='6', font=my_font_2, width=2, height=1, \
                    command=lambda: insert_to_entry('6'))
button_6.grid(row=2, column=2, padx=2, pady=2)

button_7 = Button(window, text='7', font=my_font_2, width=2, height=1, \
                    command=lambda: insert_to_entry('7'))
button_7.grid(row=3, column=0, padx=2, pady=2)

button_8 = Button(window, text='8', font=my_font_2, width=2, height=1, \
                    command=lambda: insert_to_entry('8'))
button_8.grid(row=3, column=1, padx=2, pady=2)

button_9 = Button(window, text='9', font=my_font_2, width=2, height=1, \
                    command=lambda: insert_to_entry('9'))
button_9.grid(row=3, column=2, padx=2, pady=2)

button_0 = Button(window, text='0', font=my_font_2, width=2, height=1, \
                    command=lambda: insert_to_entry('0'))
button_0.grid(row=4, column=1, padx=2, pady=2)

button_clear = Button(window, text='C', font=my_font_2, width=2, height=1, bg='red', \
                    command=clear_entry)
button_clear.grid(row=4, column=0, padx=2, pady=2)

button_dot = Button(window, text='.', font=my_font_2, width=2, height=1, \
                    command=lambda: insert_to_entry('.'))
button_dot.grid(row=4, column=2, padx=2, pady=2)

button_plus = Button(window, text='+', font=my_font_2, width=2, height=1, bg='yellow', \
                    command=lambda: insert_to_entry('+'))
button_plus.grid(row=1, column=3, padx=2, pady=2)

button_minus = Button(window, text='-', font=my_font_2, width=2, height=1, bg='yellow', \
                    command=lambda: insert_to_entry('-'))
button_minus.grid(row=2, column=3, padx=2, pady=2)

button_multiply = Button(window, text='*', font=my_font_2, width=2, height=1, bg='yellow', \
                    command=lambda: insert_to_entry('*'))
button_multiply.grid(row=3, column=3, padx=2, pady=2)

button_division = Button(window, text='/', font=my_font_2, width=2, height=1, bg='yellow', \
                    command=lambda: insert_to_entry('/'))
button_division.grid(row=4, column=3, padx=2, pady=2)


button_equal = Button(window, text='=', font=my_font_2, width=2, height=1, bg='blue', \
                    command=show_result)
button_equal.grid(row=1, column=4, rowspan=4, padx=2, pady=2, sticky=N+S)

window.mainloop()
