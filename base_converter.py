from tkinter import *
from tkinter import messagebox

root = Tk()
root.resizable(width=False,height=False)
root.configure(background="black")
label_1 = Label(root, text="	Enter value: ",background="black",fg="white",font=('arial',13,'bold'))
label_1.grid(row=0, sticky=W)

label_space = Label(root, text=" ",background="black",fg="white",font=('arial',13,'bold'))
label_space.grid(row=0, column=1)

entry = Entry(root, bd=10,background='black',fg="white",font=('arial',12,'bold'))
entry.grid(row=0, column=1, columnspan=2, ipadx=30, ipady=5)


def backspace():
    entry.delete(entry.index(INSERT) - 1)


btn_backspace = Button(root, text="<-- Backspace", bd=5, relief="groove", bg="grey", width=15, command=backspace)
btn_backspace.grid(row=0, column=4)

def reset():
    entry.delete(0, END)
    entry.insert(0, "")

    label_space1 = Label(root, text="                   ")
    label_space2 = Label(root, text="                   ")
    label_space3 = Label(root, text="                   ")
    label_space4 = Label(root, text="                   ")
    label_space1.grid(row=9, column=2)
    label_space2.grid(row=10, column=2)
    label_space3.grid(row=11, column=2)
    label_space4.grid(row=12, column=2)

    label_NIL1 = Label(root, text="              NIL               ",background="black",fg="white",font=('arial',13,'bold'))
    label_NIL2 = Label(root, text="              NIL               ",background="black",fg="white",font=('arial',13,'bold'))
    label_NIL3 = Label(root, text="              NIL               ",background="black",fg="white",font=('arial',13,'bold'))
    label_NIL4 = Label(root, text="              NIL               ",background="black",fg="white",font=('arial',13,'bold'))
    label_NIL1.grid(row=9, column=2)
    label_NIL2.grid(row=10, column=2)
    label_NIL3.grid(row=11, column=2)
    label_NIL4.grid(row=12, column=2)

    for i in range(4):
        var_a[i].set(0)
        var_b[i].set(0)


label_space.grid(row=0, column=3)

button_reset = Button(root, text="RESET", bd=5, relief="raised", bg="red",width=15, command=reset)
button_reset.grid(row=1, column=4)

label_space.grid(row=1)

label_2 = Label(root, text="Convert Base From:",background="black",fg="white",font=('arial',13,'bold'))
label_2.grid(row=2)

label_3 = Label(root, text="Convert Base To:",background="black",fg="white",font=('arial',13,'bold'))
label_3.grid(row=2, column=2)


# ********************* ALL CONVERTING FUNCTIONS START *************************


def bin_to_bin(b):
    return (bin(int(str(b), 2)))


def bin_to_dec(b):
    return int(str(b), 2)


def bin_to_oct(b):
    return oct(int(str(b), 2))


def bin_to_hex(b):
    return hex(int(str(b), 2))


def dec_to_bin(d):
    return bin(int(d))


def dec_to_dec(d):
    return int(d)


def dec_to_oct(d):
    return oct(int(d))


def dec_to_hex(d):
    return hex(int(d))


def oct_to_bin(o):
    return bin(int(str(o), 8))


def oct_to_dec(o):
    return int(str(o), 8)


def oct_to_oct(o):
    return oct(int(str(o), 8))


def oct_to_hex(o):
    return hex(int(str(o), 8))


def hex_to_bin(h):
    return bin(int(str(h), 16))


def hex_to_dec(h):
    return int(str(h), 16)


def hex_to_oct(h):
    return oct(int(str(h), 16))


def hex_to_hex(h):
    return hex(int(str(h), 16))


# ********************* ALL CONVERTING FUNCTIONS STOP *************************

def convert():
    filename = "HISTORY.txt"
    label_space: Label = Label(root, text="                   ",bg="black",fg="white",font=('arial',13,'bold'))
    label_NIL_a = Label(root, text="              NIL               ",bg="black",fg="white",font=('arial',13,'bold'))
    label_NIL_b = Label(root, text="              NIL               ",bg="black",fg="white",font=('arial',13,'bold'))
    label_NIL_c = Label(root, text="              NIL               ",bg="black",fg="white",font=('arial',13,'bold'))

    if entry.get() == "":
        messagebox.showinfo("EMPTY", "Please enter value.")

    elif var_a[0].get() == 1 and var_b[0].get() == 1:
        try:
            label_answer = Label(root,background='black',fg='lime',font=('arial',15,'bold'), text=bin_to_bin(entry.get())[2:])
            label_space.grid(row=9, column=2)
            label_NIL_a.grid(row=10, column=2)
            label_NIL_b.grid(row=11, column=2)
            label_NIL_c.grid(row=12, column=2)
            label_answer.grid(row=9, column=2)
            file = open(filename,"a")
            file.write("Binary To Binary: "+str(entry.get())+" => "+str(bin_to_bin(entry.get())[2:])+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly '0' and '1' are accepted.\nOnly integers are allowed")

    elif var_a[0].get() == 1 and var_b[1].get() == 1:
        try:
            label_answer = Label(root, background='black',fg='lime',font=('arial',15,'bold'),text=bin_to_dec(entry.get()))
            label_NIL_a.grid(row=9, column=2)
            label_space.grid(row=10, column=2)
            label_NIL_b.grid(row=11, column=2)
            label_NIL_c.grid(row=12, column=2)
            label_answer.grid(row=10, column=2)
            file = open(filename, "a")
            file.write("Binary To Decimal: " + str(entry.get()) + " => " + str(bin_to_dec(entry.get()))+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly '0' and '1' are accepted.\nOnly integers are allowed")

    elif var_a[0].get() == 1 and var_b[2].get() == 1:
        try:
            label_answer = Label(root,background='black',fg='lime',font=('arial',15,'bold'), text=bin_to_oct(entry.get())[2:])
            label_NIL_a.grid(row=9, column=2)
            label_NIL_b.grid(row=10, column=2)
            label_space.grid(row=11, column=2)
            label_NIL_c.grid(row=12, column=2)
            label_answer.grid(row=11, column=2)
            file = open(filename, "a")
            file.write("Binary To Octal: " + str(entry.get()) + " => " + str(bin_to_oct(entry.get())[2:])+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly '0' and '1' are accepted.\nOnly integers are allowed")
    elif var_a[0].get() == 1 and var_b[3].get() == 1:
        try:
            label_answer = Label(root,background='black',fg='lime',font=('arial',15,'bold'), text=bin_to_hex(entry.get()).upper()[2:])
            label_NIL_c.grid(row=9, column=2)
            label_NIL_a.grid(row=10, column=2)
            label_NIL_b.grid(row=11, column=2)
            label_space.grid(row=12, column=2)
            label_answer.grid(row=12, column=2)
            file = open(filename, "a")
            file.write("Binary To Hexa Decimal: " + str(entry.get()) + " => " + str(bin_to_hex(entry.get()).upper()[2:])+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly '0' and '1' are accepted.\nOnly integers are allowed")

    elif var_a[1].get() == 1 and var_b[0].get() == 1:
        try:
            label_answer = Label(root,background='black',fg='lime',font=('arial',15,'bold'), text=dec_to_bin(entry.get())[2:])
            label_space.grid(row=9, column=2)
            label_NIL_a.grid(row=10, column=2)
            label_NIL_b.grid(row=11, column=2)
            label_NIL_c.grid(row=12, column=2)
            label_answer.grid(row=9, column=2)
            file = open(filename, "a")
            file.write("Decimal To Binary: " + str(entry.get()) + " => " + str(dec_to_bin(entry.get())[2:])+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly numbers are accepted.\nOnly integers are allowed")

    elif var_a[1].get() == 1 and var_b[1].get() == 1:
        try:
            label_answer = Label(root,background='black',fg='lime',font=('arial',15,'bold'), text=dec_to_dec(entry.get()))
            label_NIL_a.grid(row=9, column=2)
            label_space.grid(row=10, column=2)
            label_NIL_b.grid(row=11, column=2)
            label_NIL_c.grid(row=12, column=2)
            label_answer.grid(row=10, column=2)
            file = open(filename, "a")
            file.write("Decimal To Decimal: " + str(entry.get()) + " => " + str(dec_to_dec(entry.get()))+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly numbers are accepted.\nOnly integers are allowed")

    elif var_a[1].get() == 1 and var_b[2].get() == 1:
        try:
            label_answer = Label(root,background='black',fg='lime',font=('arial',15,'bold'), text=dec_to_oct(entry.get())[2:])
            label_NIL_a.grid(row=9, column=2)
            label_NIL_b.grid(row=10, column=2)
            label_space.grid(row=11, column=2)
            label_NIL_c.grid(row=12, column=2)
            label_answer.grid(row=11, column=2)
            file = open(filename, "a")
            file.write("Decimal To Octal: " + str(entry.get()) + " => " + str(dec_to_oct(entry.get())[2:])+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly numbers are accepted\nOnly integers are allowed")

    elif var_a[1].get() == 1 and var_b[3].get() == 1:
        try:
            label_answer = Label(root,background='black',fg='lime',font=('arial',15,'bold'), text=dec_to_hex(entry.get()).upper()[2:])
            label_NIL_c.grid(row=9, column=2)
            label_NIL_a.grid(row=10, column=2)
            label_NIL_b.grid(row=11, column=2)
            label_space.grid(row=12, column=2)
            label_answer.grid(row=12, column=2)
            file = open(filename, "a")
            file.write("Decimal To Hexa Decimal: " + str(entry.get()) + " => " + str(dec_to_hex(entry.get()).upper()[2:])+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly numbers are accepted.\nOnly integers are allowed")

    elif var_a[2].get() == 1 and var_b[0].get() == 1:
        try:
            label_answer = Label(root,background='black',fg='lime',font=('arial',15,'bold'), text=oct_to_bin(entry.get())[2:])
            label_space.grid(row=9, column=2)
            label_NIL_a.grid(row=10, column=2)
            label_NIL_b.grid(row=11, column=2)
            label_NIL_c.grid(row=12, column=2)
            label_answer.grid(row=9, column=2)
            file = open(filename, "a")
            file.write("Octal To Binary: " + str(entry.get()) + " => " + str(oct_to_bin(entry.get())[2:])+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly 0 to 7 numbers are accepted.\nOnly integers are allowed")

    elif var_a[2].get() == 1 and var_b[1].get() == 1:
        try:
            label_answer = Label(root,background='black',fg='lime',font=('arial',15,'bold'), text=oct_to_dec(entry.get()))
            label_NIL_a.grid(row=9, column=2)
            label_space.grid(row=10, column=2)
            label_NIL_b.grid(row=11, column=2)
            label_NIL_c.grid(row=12, column=2)
            label_answer.grid(row=10, column=2)
            file = open(filename, "a")
            file.write("Octal To Decimal: " + str(entry.get()) + " => " + str(oct_to_dec(entry.get()))+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly 0 to 7 numbers are accepted.\nOnly integers are allowed")

    elif var_a[2].get() == 1 and var_b[2].get() == 1:
        try:
            label_answer = Label(root,background='black',fg='lime',font=('arial',15,'bold'), text=oct_to_oct(entry.get())[2:])
            label_NIL_a.grid(row=9, column=2)
            label_NIL_b.grid(row=10, column=2)
            label_space.grid(row=11, column=2)
            label_NIL_c.grid(row=12, column=2)
            label_answer.grid(row=11, column=2)
            file = open(filename, "a")
            file.write("Octal To Ocatl: " + str(entry.get()) + " => " + str(oct_to_oct(entry.get())[2:])+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly 0 to 7 numbers are accepted.\nOnly integers are allowed")

    elif var_a[2].get() == 1 and var_b[3].get() == 1:
        try:
            label_answer = Label(root,background='black',fg='lime',font=('arial',15,'bold'),text=oct_to_hex(entry.get()).upper()[2:])
            label_NIL_c.grid(row=9, column=2)
            label_NIL_a.grid(row=10, column=2)
            label_NIL_b.grid(row=11, column=2)
            label_space.grid(row=12, column=2)
            label_answer.grid(row=12, column=2)
            file = open(filename, "a")
            file.write("Octal To Hexa Decimal: " + str(entry.get()) + " => " + str(oct_to_hex(entry.get()).upper()[2:])+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT", "You have entered invalid input.\nOnly 0 to 7 numbers are accepted.\nOnly integers are allowed")

    elif var_a[3].get() == 1 and var_b[0].get() == 1:
        try:
            label_answer = Label(root,background='black',fg='lime',font=('arial',15,'bold'),text=hex_to_bin(entry.get())[2:])
			
            label_space.grid(row=9, column=2)
            label_NIL_a.grid(row=10, column=2)
            label_NIL_b.grid(row=11, column=2)
            label_NIL_c.grid(row=12, column=2)
            label_answer.grid(row=9, column=2,pady=1)
            file = open(filename, "a")
            file.write("Hexa Decimal To Binary: " + str(entry.get()) + " => " + str(hex_to_bin(entry.get())[2:])+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT",
                                "You have entered invalid input.\nOnly 0 to 9 and 'A' to 'F' are accepted.\nOnly integers are allowed")

    elif var_a[3].get() == 1 and var_b[1].get() == 1:
        try:
            label_answer = Label(root,background='black',fg='lime',font=('arial',15,'bold'), text=hex_to_dec(entry.get()))
            label_NIL_a.grid(row=9, column=2)
            label_space.grid(row=10, column=2)
            label_NIL_b.grid(row=11, column=2)
            label_NIL_c.grid(row=12, column=2)
            label_answer.grid(row=10, column=2)
            file = open(filename, "a")
            file.write("Hexa Decimal To Decimal: " + str(entry.get()) + " => " + str(hex_to_dec(entry.get()))+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT",
                                "You have entered invalid input.\nOnly 0 to 9 and 'A' to 'F' are accepted.\nOnly integers are allowed")

    elif var_a[3].get() == 1 and var_b[2].get() == 1:
        try:
            label_answer = Label(root,background='black',fg='lime',font=('arial',15,'bold'), text=hex_to_oct(entry.get())[2:])
            label_NIL_a.grid(row=9, column=2)
            label_NIL_b.grid(row=10, column=2)
            label_space.grid(row=11, column=2)
            label_NIL_c.grid(row=12, column=2)
            label_answer.grid(row=11, column=2)
            file = open(filename, "a")
            file.write("Hexa Decimal To Octal: " + str(entry.get()) + " => " + str(hex_to_oct(entry.get())[2:])+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT",
                                "You have entered invalid input.\nOnly 0 to 9 and 'A' to 'F' are accepted.\n Only integers are allowed")

    elif var_a[3].get() == 1 and var_b[3].get() == 1:
        try:
            label_answer = Label(root,background='black',fg='lime',font=('arial',15,'bold'), text=hex_to_hex(entry.get()).upper()[2:])
            label_NIL_c.grid(row=9, column=2)
            label_NIL_a.grid(row=10, column=2)
            label_NIL_b.grid(row=11, column=2)
            label_space.grid(row=12, column=2)
            label_answer.grid(row=12, column=2)
            file = open(filename, "a")
            file.write("Hexa Decimal To Hexa Decimal: " + str(entry.get()) + " => " + str(hex_to_hex(entry.get()).upper()[2:])+"\n")
            file.close()
        except:
            messagebox.showinfo("ERROR INPUT","You have entered invalid input.\nOnly 0 to 9 and 'A' to 'F' are accepted.\n Only integers are allowed")

    else:
        messagebox.showinfo("REQUIREMENT", "Choose options on the both side")


# ***************************************************** LOOP ON GRID START ****************************************

now_a = None
buttons_a = None
var_a1 = IntVar()
var_a2 = IntVar()
var_a3 = IntVar()
var_a4 = IntVar()

var_a = [var_a1, var_a2, var_a3, var_a4]


def cb_a():
    global now_a, buttons_a
    if None != now_a:
        buttons_a[now_a].deselect()
    vals_a = [var_a[i].get() for i in range(4)]
    try:
        now_a = vals_a.index(1)
    except ValueError:
        now_a = None


x_a = ["Binary           ", "Decimal         ", "Octal             ", "Hexa Decimal"]
y_a = 3
buttons_a = [Checkbutton(root, text=x_a[i], variable=var_a[i], command=cb_a,background="grey",bd=4,font=('arial',13,'bold')) for i in range(4)]
for b in buttons_a:
    b.grid(row=y_a, sticky=W)
    y_a = y_a + 1

# *************** A SEPERATES B ***************

now_b = None
buttons_b = None
var_a1 = IntVar()
var_a2 = IntVar()
var_a3 = IntVar()
var_a4 = IntVar()

var_b = [var_a1, var_a2, var_a3, var_a4]


def cb_b():
    global now_b, buttons_b
    if None != now_b:
        buttons_b[now_b].deselect()
    vals_b = [var_b[i].get() for i in range(4)]
    try:
        now_b = vals_b.index(1)
    except ValueError:
        now_b = None


x_b = ["Binary           ", "Decimal         ", "Octal             ", "Hexa Decimal"]
y_b = 3
buttons_b = [Checkbutton(root, text=x_b[i], variable=var_b[i], command=cb_b,background="grey",bd=4,font=('arial',13,'bold')) for i in range(4)]
for b in buttons_b:
    b.grid(row=y_b, column=2, sticky=W)
    y_b = y_b + 1

# ***************************************************** LOOP ON GRID STOP ****************************************
# ***************************************************** START OF RESULT SECTION ***************************************

button_convert = Button(root, text="CONVERT", bd=5, relief="raised", bg="cyan", width=15,  command=convert)
button_convert.grid(row=7, columnspan=3)


label_space.grid(row=8)

l_bin = Label(root, text="Binary: ",background="black",fg="white",font=('arial',13,'bold'))
l_bin.grid(row=9, sticky=W)
l_bin_ans = Label(root, text="                  NIL                   ", borderwidth=3, height=2, relief="groove",background="black",fg="white",font=('arial',13,'bold'))
l_bin_ans.grid(row=9, column=2)

l_dec = Label(root, text="Decimal: ",background="black",fg="white",font=('arial',13,'bold'))
l_dec.grid(row=10, sticky=W)
l_dec_ans = Label(root, text="                  NIL                   ", borderwidth=3, height=2, relief="groove",background="black",fg="white",font=('arial',13,'bold'))
l_dec_ans.grid(row=10, column=2)

l_oct = Label(root, text="Octal: ",background="black",fg="white",font=('arial',13,'bold'))
l_oct.grid(row=11, sticky=W)
l_oct_ans = Label(root, text="                  NIL                   ", borderwidth=3, height=2, relief="groove",background="black",fg="white",font=('arial',13,'bold'))
l_oct_ans.grid(row=11, column=2)

l_hex = Label(root, text="Hexa Decimal: ",background="black",fg="white",font=('arial',13,'bold'))
l_hex.grid(row=12, sticky=W)
l_hex_ans = Label(root, text="                  NIL                   ", borderwidth=3, height=2, relief="groove",background="black",fg="white",font=('arial',13,'bold'))
l_hex_ans.grid(row=12, column=2)

root.title("Base Converter")
try:
    root.iconbitmap("gnu.ico")
except:
    pass


# ***************************************************** END OF RESULT SECTION ***************************************

def history():
    try:
        filename = "HISTORY.txt"
        file = open(filename, "r")
        data = file.readlines()
        m = ""
        for i in data:
            m = m + str(i) + "\n"
        messagebox.showinfo("HISTORY", str(m))
        file.close()
    except:
        messagebox.showinfo("EMPTY","There are no histoty recorded.")


btn_history = Button(root, text="HISTORY", bd=5, width=15, bg="grey", relief="raised", command=history)
btn_history.grid(row=2	, column=4)


def about():
    messagebox.showinfo("ABOUT","Developed BY DHARMAY SUREJA")

btn_about = Button(root, text="ABOUT", bd=5, width=15, bg="grey", relief="raised", command=about)
btn_about.grid(row=3, column=4)

btn_exit = Button(root, text="EXIT", bd=5, width=15, bg="red", relief="raised", command=root.destroy)
btn_exit.grid(row=4, column=4)

root.mainloop()
