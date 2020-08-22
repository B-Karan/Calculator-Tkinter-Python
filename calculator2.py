from tkinter import *


BUTTON_COLOR = "#bfbfbd"
BG_COLOR = "#e3e1dc"

root = Tk()
root.title("Calculator")
root.resizable(0, 0)

#Setting background color of root window
root.configure(background=BG_COLOR)
# root.iconbitmap('calculator_ico.ico')
root.iconphoto(True, PhotoImage(file='calculator.png'))

# Entry field for getting inputs
input = Entry(root, width = 45, borderwidth = 3)
input.grid(row = 0, column = 0, columnspan = 4, padx=10, pady=10, ipady=10)

# Frame for numbers
nums_frame = LabelFrame(root, bd=0, bg=BG_COLOR)
nums_frame.grid(row=1, column=0, padx=3, pady=5)

# Frame for operations
right_frame = LabelFrame(root, bd=0, bg=BG_COLOR)
right_frame.grid(row=1, column=1)


def clear_input():
    '''
    Clears the input field
    '''
    input.delete(0, END)

def number_click(number):
    '''
    Displays the entered numbers on input field
    '''
    current = input.get()
    clear_input()
    input_number = current + str(number)
    input.insert(0, input_number)

def get_first_number():
    '''
    Stores the first number entered in first number
    '''
    number = input.get()
    global first_number
    first_number = int(number)
    clear_input()

def and_op():
    ''' Assigns '&' operation '''
    get_first_number()
    global operation
    operation = "&"
    clear_input()

def or_op():
    ''' Assigns '|' operation'''
    get_first_number()
    global operation
    operation = "|"
    clear_input()

def xor_op():
    '''Assigns XOR operation'''
    get_first_number()
    global operation
    operation = "xor"
    clear_input()

def ls_op():
    '''Assigns Left Shift Operation'''
    get_first_number()
    global operation
    operation = "<<"
    clear_input()

def rs_op():
    '''Assigns Left Shift Operation'''
    get_first_number()
    global operation
    operation = ">>"
    clear_input()

def fact_op():
    ''' Performs factorial'''
    get_first_number()
    fact=1
    for i in range(1, first_number+1):
        fact *= i
    input.insert(0, fact)

def sqr_op():
    '''Performs squaring of number'''
    get_first_number()
    input.insert(0, first_number**2)
def pwr_op():
    '''Power of a number'''
    get_first_number()
    global operation
    operation = "pwr"
    clear_input()

def add():
    ''' Assigns '+' operation'''
    get_first_number()
    global operation
    operation = "+"
    clear_input()

def subtract():
    ''' Assigns '-' operation'''
    get_first_number()
    global operation
    operation = "-"
    clear_input()

def division():
    ''' Assigns '/' operation'''
    get_first_number()
    global operation
    operation = "/"
    clear_input()

def multplication():
    ''' Assigns '*' operation'''
    get_first_number()
    global operation
    operation = "*"
    clear_input()

def equal():
    ''' Takes second number and performs the operation'''
    number = input.get()
    clear_input()
    second_number = int(number)
    if operation == "+":
        answer = first_number + second_number
    elif operation == "-":
        answer = first_number - second_number
    elif operation == "/":
        answer = float(first_number / second_number)
    elif operation == "*":
        answer = first_number * second_number
    elif operation == "&":
        answer = first_number & second_number
    elif operation == "|":
        answer = first_number | second_number
    elif operation == "xor":
        answer = first_number ^ second_number
    elif operation == "pwr":
        answer = first_number ** second_number
    elif operation == "<<":
        answer = first_number << second_number
    elif operation == ">>":
        answer = first_number >> second_number
    input.insert(0, answer)


digits = [Button(nums_frame, text=str(i), padx=25, pady=10, command=lambda i=i: number_click(i), bg=BUTTON_COLOR) for i in range(10)]


button_clear = Button(right_frame, text="CLR", padx=23, pady=15, command=clear_input, bg="#8cf59a")
button_equal = Button(right_frame, text="=", padx=30, pady=15, command=equal, bg="#99ebff")

button_add = Button(right_frame, text="+", padx=29, pady=15, command=add, bg="#ede73e")
button_subtract = Button(right_frame, text="-", padx=30, pady=15, command=subtract, bg="#ede73e")
button_mult = Button(right_frame, text="x", padx=30, pady=15, command=multplication, bg="#ede73e")
button_div = Button(right_frame, text="/", padx=30, pady=15, command=division, bg="#ede73e")

digits[0].grid(row=3, column=1, padx = 3, pady = 3)
digits[1].grid(row = 6, column = 0, padx = 3, pady = 3)
digits[2].grid(row = 6, column = 1, padx = 3, pady = 3)

digits[3].grid(row = 6, column = 2, padx = 3, pady = 3)
digits[4].grid(row = 5, column = 0, padx = 3, pady = 3)
digits[5].grid(row = 5, column = 1, padx = 3, pady = 3)

digits[6].grid(row = 5, column = 2, padx = 3, pady = 3)
digits[7].grid(row = 4, column = 0, padx = 3, pady = 3)
digits[8].grid(row = 4, column = 1, padx = 3, pady = 3)
digits[9].grid(row = 4, column = 2, padx = 3, pady = 3)

button_and = Button(nums_frame, text=" --- ", padx=16, pady=10, bg=BUTTON_COLOR)
button_and.grid(row=0, column=0, padx = 3, pady = 3)

button_or = Button(nums_frame, text="--- ", padx=19, pady=10, bg=BUTTON_COLOR)
button_or.grid(row=0, column=1, padx = 3, pady = 3)

button_xor = Button(nums_frame, text=" --- ", padx=16, pady=10, bg=BUTTON_COLOR)
button_xor.grid(row=0, column=2, padx = 3, pady = 3)

button_and = Button(nums_frame, text="AND", padx=16, pady=10, command=and_op, bg=BUTTON_COLOR)
button_and.grid(row=1, column=0, padx = 3, pady = 3)

button_or = Button(nums_frame, text="OR", padx=19, pady=10, command=or_op, bg=BUTTON_COLOR)
button_or.grid(row=1, column=1, padx = 3, pady = 3)

button_xor = Button(nums_frame, text="XOR", padx=16, pady=10, command=xor_op, bg=BUTTON_COLOR)
button_xor.grid(row=1, column=2, padx = 3, pady = 3)

button_sqr = Button(nums_frame, text="x^2", padx=17, pady=10, command=sqr_op, bg=BUTTON_COLOR)
button_sqr.grid(row=2, column=0, padx = 3, pady = 3)

button_pwr = Button(nums_frame, text="x^n", padx=17, pady=10, command=pwr_op, bg=BUTTON_COLOR)
button_pwr.grid(row=2, column=1, padx = 3, pady = 3)

button_fact = Button(nums_frame, text=" ! ", padx=24, pady=10, command=fact_op, bg=BUTTON_COLOR)
button_fact.grid(row=2, column=2, padx = 3, pady = 3)

button_ls = Button(nums_frame, text="<<", padx=20, pady=10, command=ls_op, bg=BUTTON_COLOR)
button_ls.grid(row=3, column=0, padx = 3, pady = 3)

button_rs = Button(nums_frame, text=">>", padx=20, pady=10, command=rs_op, bg=BUTTON_COLOR)
button_rs.grid(row=3, column=2, padx = 3, pady = 3)

button_add.grid(row = 0, column = 0, padx = 3, pady = 3)
button_subtract.grid(row = 1, column = 0, padx = 3, pady = 3)
button_mult.grid(row = 2, column = 0, padx = 3, pady = 3)
button_div.grid(row = 3, column = 0, padx = 3, pady = 3)

button_clear.grid(row = 4, column = 0, columnspan = 2, padx = 3, pady = 3)
button_equal.grid(row = 5, column = 0, columnspan = 2, padx = 3, pady = 3)

root.mainloop()
