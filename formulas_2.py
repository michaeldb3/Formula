__author__ = 'Mike'; 'Intuitive Design'

import logging
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.simpledialog import askstring
import math
import tkinter.messagebox

# Variables & Core objects section
#   tk(), and ttk():
root = Tk()
root.config(bg='light grey')
root2 = ttk
s = ttk.Style()
s.theme_use('clam')
s.configure('TButton', background="grey32", fg="white")
#   ______________
#   Frames:
frame = Frame(root)
frame2 = Frame(root, pady=10, width=400)
frame2.config(bg="grey10")
#   ______________
#   Program window:
root.title("Formula")
root.iconbitmap('pi-outline-128.ico')
#   ______________
#   Other:
box = tkinter.messagebox
output_txt = "Output here"
pi = math.pi
underscore = "_________________________________"
unnecessary = 1
code_to_get = 2
key_binding_to_work = 3
#   _______________
string_num = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
              'nine': '9', 'ten': '10', 'eleven': '11', 'twelve': '12', 'thirteen': '13', 'fourteen': '14',
              'fifteen': '15', 'sixteen': '16', "seventeen": '17', 'eighteen': '18', 'eightteen': '18', 'nineteen': '19'
              , 'twenty': '20', 'twenty-one': '21', 'twenty-two': '22', 'twenty-three': '23', 'twenty-four': '24',
              'twenty-five': '25', 'twenty-six': '26', 'twenty-seven': '27', 'twenty-eight': '28', 'twenty-nine': '29',
              'thirty': '30', 'thirty-one': '31', 'thirty-two': '32', 'thirty-three': '33', 'thirty-four': '34',
              'thirty-five': '35', 'thirty-six': '36', 'thirty-seven': '37', 'thirty-eight': '38', 'thirty-nine': '39',
              'forty': '40', 'fourty': '40', 'forty-one': '41', 'forty-two': '42', 'forty-three': '43', 'forty-four':
              '44', 'forty-five': '45', 'forty-six': '46', 'forty-seven': '47', 'forty-eight': '48', 'forty-nine': '49',
              'fifty': '50', 'sixty': '60', 'seventy': '70', 'eighty': '80', 'ninety': '90', 'one-hundred': '100',
              'one-thousand': '1000', 'ten-thousand': '10000', 'one-hundred-thousand': '100000',
              'one-million': '1000000', 'one-billion': '1000000000', 'one-trillion': '1000000000000', 'vegeta':
              '9000', 'dragon-ball-z': '9000', 'goku': '9000'}
# ---(end of variable section)-----------------------

#   Functions: -----
args = [unnecessary, code_to_get, key_binding_to_work]
def radius_input(*args):
    try:
        output = entry_pi.get()
        radius = float(output)
    except ValueError:
        try:
            if ord(output[0]) >= 65 and ord(output[0]) <= 90:
                replacement = chr((ord(output[0]) + 32))
                output = output.replace(output[0], replacement)
            if " " in output:
                output = output.replace(" ", "-")
            output = output.replace(output, string_num[output])
            radius = float(output)
            logging.warning('ValueError corrected')

        except KeyError:
            try:
                if output[1] == '/':
                    first_num = int(output[0])
                    second_num = int(output[2])
                    answer = first_num / second_num
                    radius = float(answer)
                    logging.warning('KeyError corrected')
                else:
                    box.showinfo("Error Occurred", "Sorry, you forgot the input or caused an unknown error!")
                    logging.warning("Invalid input from entry_pi.get")
            except Exception:
                pass
    try:
        A = pi * (radius ** 2)
        A_spec = "{:,.5f}".format(A)
        # ------Background info (True value of circle's area; no rounding at all -----
        print("True Value: ", A, "\n", underscore)
        # ----------------------------------------------------------------------------
        print("Specific Value:", A_spec, "\n", underscore)
        entry_pi_out.delete(0, 100)
        entry_pi_out2.delete(0, 100)
        entry_pi_out.insert(0, A_spec)

        if A < A // 1 + 0.499995:
            A_rounddown = (A // 1)
            A_rounddown = "{:,}".format(A_rounddown)
            print("Rounded Value:", A_rounddown, "\n", underscore, "\n")
            entry_pi_out2.insert(0, A_rounddown)

        elif A >= A // 1 + 0.499995:
            A_roundup = (A // 1) + 1.0
            A_roundup = "{:,}".format(A_roundup)
            print("Rounded Value:", A_roundup, "\n", underscore, "\n")
            entry_pi_out2.insert(0, A_roundup)
        else:
            # You created an interesting error...
            box.showinfo("Easter Egg", """Read the console, command prompt, and run-time in the
            I.D.E for something silly""")
            logging.warning("""If you happen to somehow encounter this error, enjoy this boring easter egg! \n
                Fun Fact: \n Please note that any float number with a decimal value that rounds to or is directly
                equal to ([A // 1] + 0.890456602957145) creates difficulties that required 0.499995 to be used in the
                rounding process""")
        hist_A = str(A_spec)
        form_radius = "{:,}".format(radius)
        hist_r = str(form_radius)
        # π - storing the pi symbol in comment due to unicode string errors
        pie = u"π"
        hist_math = hist_r + "(r)" + "^2 * " + pie + " = " + hist_A + "\n"
        hist_prompt = hist_math
        history.insert(1.0, hist_prompt)
    except UnboundLocalError:
        pass


args = [unnecessary, code_to_get, key_binding_to_work]
def distance(*args):
    try:
        r = entry_rate.get()
        int_r = float(r)
    except ValueError:
        try:
            if ord(r[0]) >= 65 and ord(r[0]) <= 90:
                replacement = chr((ord(r[0]) + 32))
                r = r.replace(r[0], replacement)
            if " " in r:
                r = r.replace(" ", "-")
            r = r.replace(r, string_num[r])
            int_r = float(r)
            logging.warning('ValueError corrected')
        except KeyError:
            try:
                if r[1] == '/':
                    first_num = int(r[0])
                    second_num = int(r[2])
                    answer = first_num / second_num
                    int_r = float(answer)
                    logging.warning('KeyError corrected')
                else:
                    box.showinfo("Error Occurred", "Sorry, you forgot the input or caused an unknown error!")
                    logging.warning("Invalid input from entry_rate.get")
            except Exception:
                pass
    try:
        t = entry_time.get()
        int_t = float(t)
    except ValueError:
        try:
            if ord(t[0]) >= 65 and ord(t[0]) <= 90:
                replacement = chr((ord(t[0]) + 32))
                t = t.replace(t[0], replacement)
            if " " in t:
                t = t.replace(" ", "-")
            t = t.replace(t, string_num[t])
            int_t = float(t)
            logging.warning('ValueError corrected')
        except KeyError:
            try:
                if t[1] == '/':
                    first_num = int(t[0])
                    second_num = int(t[2])
                    answer = first_num / second_num
                    int_t = float(answer)
                    logging.warning('KeyError corrected')
                else:
                    box.showinfo("Error Occurred", "Sorry, you forgot the input or caused an unknown error!")
                    logging.warning("Invalid input from entry_rate.get")
            except Exception:
                pass
    try:
        D = int_r * int_t
        form_D = "{:,.2f}".format(D)
        print(form_D)
        entry_dist.delete(0, 100)
        entry_dist.insert(0, form_D)
        form_r = "{:,.2f}".format(int_r)
        form_t = "{:,.2f}".format(int_t)
        hist_prompt = form_r + "(r)" + " * " + form_t + "(t)" + " = " + form_D + "\n"
        history.insert(1.0, hist_prompt)
    except UnboundLocalError:
        pass
    '''
    except ValueError:
        box.showinfo("Error Occurred", "Sorry, you forgot the input or caused an unknown error!")
        logging.warning("Sorry, you forgot the input or caused an unknown error!")
        # print("Sorry, you forgot the input or caused an unknown error!")
    '''


def leftclick(event):
    if entry_pi.get() == "Input Radius Here":
        entry_pi.delete(0, 100)
    else:
        pass


def leftclick2(event):
    if entry_pi_out.get() == "# Exact Value...":
        entry_pi_out.delete(0, 100)
    else:
        pass


def leftclick3(event):
    if entry_pi_out2.get() == "# Rounded Value ...":
        entry_pi_out2.delete(0, 100)
    else:
        pass


def leftclickdist(event):
    if entry_rate.get() == "Input Rate Here":
        entry_rate.delete(0, 100)
    else:
        pass


def leftclickdist2(event):
    if entry_time.get() == "Elapsed Time Value...":
        entry_time.delete(0, 100)
    else:
        pass


def leftclickdist3(event):
    if entry_dist.get() == "Distance Travelled":
        entry_dist.delete(0, 100)
    else:
        pass


def save():
    answer = ttk.tkinter.messagebox.askquestion("Save:", "Are you sure you want to save your history?")
    if answer == "yes":
        file_name = askstring("File Name:", "What would you like to save it as? \n Please remember to specify\
    the file type (i.e. .txt, .csv, .doc, etc.)")
        try:
            with open(file_name, 'w', encoding='utf-8') as fw:
                write_var = history.get('1.0', END)
                fw.write(write_var)
                fw.close()
        except TypeError:
            logging.warning('user cancelled file saving process')
    else:
        pass

def clearAll():
    entry_dist.delete(0, 100)
    entry_time.delete(0, 100)
    entry_rate.delete(0, 100)
    entry_pi.delete(0, 100)
    entry_pi_out.delete(0, 100)
    entry_pi_out2.delete(0, 100)
    history.delete(1.0, 10000.0)
    entry_pi.insert(0, "Input Radius Here")
    entry_pi_out.insert(0, "# Exact Value...")
    entry_pi_out2.insert(0, "# Rounded Value ...")
    entry_rate.insert(0, "Input Rate Here")
    entry_time.insert(0, "Elapsed Time Value...")
    entry_dist.insert(0, "Distance Travelled")

y = ""
def current_formula(y):
    if y == "1":
        history.grid_remove()
        history.grid(row=6, column=0, sticky="s", padx=6, pady=100)
        button1.grid(row=0, column=0, padx=10, pady=10)
        entry_pi.grid(row=0, column=1, padx=10, pady=10)
        entry_pi_out.grid(row=0, column=2, padx=10, pady=10)
        entry_pi_out2.grid(row=1, column=2, padx=10, pady=12)
        root.bind("<Return>", lambda x: radius_input(*args))
        button2.grid_remove()
        entry_rate.grid_remove()
        entry_time.grid_remove()
        entry_dist.grid_remove()
        one.config(bg="maroon")
    elif y == "2":
        history.grid_remove()
        history.grid(row=6, column=0, sticky="s", padx=6, pady=100)
        button2.grid(row=0, column=0, padx=10, pady=10)
        entry_rate.grid(row=0, column=1, padx=10, pady=10)
        entry_time.grid(row=1, column=1, padx=10, pady=10)
        entry_dist.grid(row=0, column=2, padx=10, pady=12)
        root.bind("<Return>", lambda x: distance(*args))
        button1.grid_remove()
        entry_pi.grid_remove()
        entry_pi_out.grid_remove()
        entry_pi_out2.grid_remove()
        one.config(bg="paleturquoise4")
    else:
        one.config(bg="goldenrod4")
        try:
            history.grid_remove()
            entry_pi.delete(0, 100)
            entry_pi_out.delete(0, 100)
            entry_pi_out2.delete(0, 100)
            entry_rate.delete(0, 100)
            entry_time.delete(0, 100)
            entry_dist.delete(0, 100)
            entry_pi.insert(0, "Input Radius Here")
            entry_pi_out.insert(0, "# Exact Value...")
            entry_pi_out2.insert(0, "# Rounded Value ...")
            entry_rate.insert(0, "Input Rate Here")
            entry_time.insert(0, "Elapsed Time Value...")
            entry_dist.insert(0, "Distance Travelled")
            button1.grid_forget()
            entry_pi.grid_forget()
            entry_pi_out.grid_forget()
            entry_pi_out2.grid_forget()
            button2.grid_forget()
            entry_rate.grid_forget()
            entry_time.grid_forget()
            entry_dist.grid_forget()
        finally:
            pass
'''
button1.grid(row=0, column=0, padx=10, pady=10)
entry_pi.grid(row=0, column=1, padx=10, pady=10)
entry_pi_out.grid(row=0, column=2, padx=10, pady=10)
entry_pi_out2.grid(row=1, column=2, padx=10, pady=12)
one.config(bg="maroon")
'''
# ----------------------

#   toolbar: -----
toolframe = Frame(root)
toolbar = Frame(toolframe, bg="gray7")
#   --------

#   Main: -----
#       Labels ---
one = Label(frame, pady=0, padx=20, width=31)
one_trim = Label(frame, bg="gray24", padx=1.5)
two = Label(toolbar, text="Formula", fg='gray34', font='broadway 24 bold italic', bg="gray10", pady=20, padx=20)

# complicated way to underline "Formula"... would only underline the 'o' without this... uses 'font' import @ top
f = font.Font(two, two.cget("font"))
f.configure(underline=True)
two.configure(font=f)
#       ----------

#       Button, entry boxes, answer boxes --
button1 = root2.Button(frame2, text="Area of a circle ", command=radius_input)
# very poorly written code... resulted in a random *args parameter, lambda statement, and the event to be bound to
# 'root' [i.e. Tk()] instead of button1. Please resolve this. *args is specified above 'radius_input()'.


entry_pi = ttk.Entry(frame2)
entry_pi.bind("<Button-1>", leftclick)

entry_pi_out = ttk.Entry(frame2)
entry_pi_out2 = ttk.Entry(frame2)
entry_pi_out.bind("<Button-1>", leftclick2)
entry_pi_out2.bind("<Button-1>", leftclick3)

button2 = root2.Button(frame2, text="Calculate Distance ", command=distance)
# same backwards *args parameter as 'button1' and 'radius_input()' suffer from are in 'button2' & 'distance()'

entry_rate = ttk.Entry(frame2)
entry_rate.bind("<Button-1>", leftclickdist)

entry_time = ttk.Entry(frame2)
entry_time.bind("<Button-1>", leftclickdist2)

entry_dist = ttk.Entry(frame2)
entry_dist.bind("<Button-1>", leftclickdist3)
#       -------------------------------------

# History text box -----
history = Text(one, height=20, width=30, spacing3=2.5)
# ----------------------------

#   --------

# Dropdown menu -------
menu = Menu(root)
root.config(menu=menu)
submenu = Menu(menu)
menu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Clear All", command=clearAll)
submenu.add_command(label="Save", command=save)
submenu.add_separator()
submenu.add_command(label="Exit", command=lambda: current_formula(""))
editmenu = Menu(menu)
menu.add_cascade(label="Formulas", menu=editmenu)
editmenu.add_command(label="Area of a circle", command=lambda: current_formula("1"))
editmenu.add_command(label="Distance Formula", command=lambda: current_formula("2"))
# ----------------------
# .pack ------
frame.pack(side="left", fill='y')
frame2.pack(side='right', fill='y')
one.pack(side='left', fill='y')
one_trim.pack(side='right', fill='y')
two.pack(side='top', pady=6)
toolbar.pack(side="top", fill="x")
toolframe.pack(side="top", fill='x', padx=4)


# ----- end/loop program & execute remnant functions -----
current_formula(y)
root.mainloop()