from tkinter import *
import dic


# must be -column, -columnspan, -in, -ipadx, -ipady, -padx, -pady, -row, -rowspan, or -sticky
# window options
window = Tk()
window.title('Dictionary')
window.geometry('400x167')
window.configure(bg='aqua')
window.resizable(width=False, height=False)
dic_Language = [('English to persian', 'e2p'), ('persian to English', 'p2e')]




# fanctions
def Go( i_=''):
    variable = var.get()
    inp = input_char.get()
    if inp == '':
        lb.delete(0, END)  # اگر listbox از قبل پر باشد آن را خالی میکند.
        lb.insert(END, 'can`t find \'\' in database.')
        lb.configure(fg='red')
        window.geometry('400x280')
        B_GO.configure(pady=0, text='translation', bd=1)
    else:
        lb.delete(0, END)  # اگر listbox از قبل پر باشد آن را خالی میکند.
        lb.configure(fg='black')
        end = dic.Database()
        for prnt in end.search(inp,end.List(),str(variable)):
            lb.insert(END,prnt) # نمایش روی listbox

        window.geometry('400x280')
        B_GO.configure(pady=0, text='translation', bd=1)
        # B_GO.pack(anchor = 'w', padx = 14)


def Advance_Search(_A_=''):
    if str(var.get()) == '0':
        var.set(1)
    else:
        var.set(0)

def Dev_info(f_):
    info_window = Toplevel(window)
    info_window.geometry('300x200')
    info_window.grab_set()
    tozihat = Label(info_window, text='Developed by mohammad hosein(mhap)\n\n please send your comments and suggestions\nabout this app to my email\nEmail address: mhap10010010@gmail.com',justify='left')
    tozihat.pack()
    info_window.mainloop()

    
Label(window, text='plaese enter character for translation.', font=('Aria', 15), bg='aqua').pack()

var = IntVar()
b = Checkbutton(window, text='Advanced Search', variable=var, bg='aqua', activebackground='aqua', bd=0)
b.pack(pady=11)

Label(window, text='Enter word: ', font=('Aria', 10), bg='aqua').pack(anchor='w', ipadx=20)

input_char = Entry(window, width=40, highlightthickness=2, selectbackground='green',selectborderwidth=1, selectforeground='white', font=('B Tahoma', 12))
input_char.pack()

B_GO = Button(window, text='Go to translation', command=Go, bg='green', fg='white', pady=7, bd=1)
B_GO.pack()



window.bind('<Return>', Go)
window.bind('<Alt-a>', Advance_Search)
window.bind('<F1>', Dev_info)
lb = Listbox(window, height=30)
lb.pack(expand=True, fill='x', pady=6, padx=6)

window.mainloop()
