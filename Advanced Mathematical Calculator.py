from tkinter import *
#from sympy.integrals import laplace_transform
from sympy import *
from sympy.integrals import *
from sympy.abc import t,s,a,x
import math

temp=0
flag=0
expression=''

def create_window(event):
    if Advance.state()==NORMAL:
        Advance.withdraw()
    else:
        Advance.deiconify()

def create_window_override():
    if Advance.state()==NORMAL:
        Advance.withdraw()
    else:
        Advance.deiconify()

#Event functions for numbers

def zero(event):
    global expression
    expression = str(value_in_widget.get()) + '0'
    value_in_widget.set(expression)

def one(event):
    global expression
    expression = str(value_in_widget.get()) + '1'
    value_in_widget.set(expression)

def two(event):
    global expression
    expression = str(value_in_widget.get()) + '2'
    value_in_widget.set(expression)

def three(event):
    global expression
    expression = str(value_in_widget.get()) + '3'
    value_in_widget.set(expression)

def four(event):
    global expression
    expression = str(value_in_widget.get()) + '4'
    value_in_widget.set(expression)

def five(event):
    global expression
    expression = str(value_in_widget.get()) + '5'
    value_in_widget.set(expression)

def six(event):
    global expression
    expression = str(value_in_widget.get()) + '6'
    value_in_widget.set(expression)

def seven(event):
    global expression
    expression = str(value_in_widget.get()) + '7'
    value_in_widget.set(expression)

def eight(event):
    global expression
    expression = str(value_in_widget.get()) + '8'
    value_in_widget.set(expression)

def nine(event):
    global expression
    expression = str(value_in_widget.get()) + '9'
    value_in_widget.set(expression)

#/Event Functions for numbers

def addition(event):
    global expression
    expression = str(value_in_widget.get())+'+'
    value_in_widget.set(expression)
    # if flag == 0:
    #     temp = float(value_in_widget.get())
    #     value_in_widget.set("");
    #     flag =1;
    # elif flag == 1:
    #     expression = temp + float(value_in_widget.get())
    #     value_in_widget.set("");
    #     temp= expression;
    #     flag =1;
    # elif flag == 2:
    #     expression = temp - float(value_in_widget.get())
    #     value_in_widget.set("");
    #     temp= expression
    #     flag =1;
    # elif flag == 3:
    #     expression = temp * float(value_in_widget.get())
    #     value_in_widget.set("");
    #     temp = expression
    #     flag = 1;
    # elif flag == 4:
    #     expression = temp / float(value_in_widget.get())
    #     value_in_widget.set("");
    #     temp = expression
    #     flag = 1;

def subtract(event):
    global expression
    expression = str(value_in_widget.get())+'-'
    value_in_widget.set(expression)

    # if flag == 0:
    #     temp = float(value_in_widget.get())
    #     value_in_widget.set("");
    #     flag = 2;
    # elif flag == 1:
    #     expression = temp + float(value_in_widget.get())
    #     value_in_widget.set("");
    #     temp = expression
    #     flag = 2;
    # elif flag == 2:
    #     expression = temp - float(value_in_widget.get())
    #     value_in_widget.set("");
    #     temp = expression
    #     flag = 2;
    # elif flag == 3:
    #     expression = temp * float(value_in_widget.get())
    #     value_in_widget.set("");
    #     temp = expression
    #     flag = 2;
    # elif flag == 4:
    #     expression = temp / float(value_in_widget.get())
    #     value_in_widget.set("");
    #     temp = expression
    #     flag = 2;


def multiply(event):
    global expression
    expression = str(value_in_widget.get())+'*'
    value_in_widget.set(expression)

    # if flag == 0:
    #     temp = float(value_in_widget.get())
    #     value_in_widget.set("");
    #     flag = 3;
    # elif flag == 1:
    #     expression = temp + float(value_in_widget.get())
    #     value_in_widget.set("");
    #     temp = expression
    #     flag = 3;
    # elif flag == 2:
    #     expression = temp - float(value_in_widget.get())
    #     value_in_widget.set("");
    #     temp = expression
    #     flag = 3;
    # elif flag == 3:
    #     expression = temp * float(value_in_widget.get())
    #     value_in_widget.set("");
    #     temp = expression
    #     flag = 3;
    # elif flag == 4:
    #     expression = temp / float(value_in_widget.get())
    #     value_in_widget.set("");
    #     temp = expression
    #     flag = 3;


def division(event):
    global expression
    expression = str(value_in_widget.get())+'/'
    value_in_widget.set(expression)

    # global expression, flag, temp
    # if flag == 0:
    #     temp = float(value_in_widget.get())
    #     value_in_widget.set("");
    #     flag = 4;
    # elif flag == 1:
    #     expression = temp + float(value_in_widget.get())
    #     value_in_widget.set("");
    #     temp = expression
    #     flag = 4
    # elif flag == 2:
    #     expression = temp - float(value_in_widget.get())
    #     value_in_widget.set("");
    #     temp = expression
    #     flag = 4
    # elif flag == 3:
    #     expression = temp * float(value_in_widget.get())
    #     value_in_widget.set("");
    #     temp = expression
    #     flag = 4
    # elif flag == 4:
    #     expression = temp / float(value_in_widget.get())
    #     value_in_widget.set("");
    #     temp = expression
    #     flag = 4;
    #

def EqualTo(event):
    global expression
    # if flag == 1:
    #     expression = temp + float(value_in_widget.get())
    #     value_in_widget.set("");
    #     temp=0
    #     flag =0;
    # elif flag == 2:
    #     expression = temp - float(value_in_widget.get())
    #     value_in_widget.set("");
    #     temp=0
    #     flag =0;
    # elif flag == 3:
    #     expression = temp * float(value_in_widget.get())
    #     value_in_widget.set("");
    #     temp=0
    #     flag =0;
    # elif flag == 4:
    #     expression = temp / float(value_in_widget.get())
    #     value_in_widget.set("");
    #     temp=0
    #     flag =0;

    expression = eval(value_in_widget.get())
    value_in_widget.set(expression);

def reset(event):
    global expression,flag,temp
    expression = 0
    flag = 0
    temp = 0
    value_in_widget.set("")

root = Tk();
root.title("Calculator")
w = 400 # width for the Tk root
h = 350 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

#NEW ADVANCED MODE WINDOW
Advance = Toplevel(root)
Advance.overrideredirect(1)
Advance.withdraw()
CentreFrame = Frame(Advance)
Advance.protocol('WM_DELETE_WINDOW', create_window_override)
dw = 400
dh = 220
dx = x +7
dy = y + h + 29
# dw = 240
# dh = 220
# dx = x +97
# dy = y + h + 29
Advance.geometry("%dx%d+%d+%d" %(dw, dh, dx , dy))

value_in_widget = StringVar();
TopFrame= Frame(root)
MidFrame= Frame(root)
BottomFrame= Frame(root)
ScreenIn = Entry(TopFrame,justify = RIGHT,textvariable = value_in_widget, width = 70)

#Number Button Definition
Zero = Button(MidFrame,height = 3, width = 10, text = '0',command = value_in_widget.set(value_in_widget.get()+'0'))
Zero.bind("<Button-1>",zero)

One = Button(MidFrame,height = 3, width = 10, text = '1')
One.bind("<Button-1>",one)

Two = Button(MidFrame,height = 3, width = 10, text = '2')
Two.bind("<Button-1>",two)

Three = Button(MidFrame,height = 3, width = 10, text = '3')
Three.bind("<Button-1>",three)

Four = Button(MidFrame,height = 3, width = 10, text = '4')
Four.bind("<Button-1>",four)

Five = Button(MidFrame,height = 3, width = 10, text = '5')
Five.bind("<Button-1>",five)

Six = Button(MidFrame,height = 3, width = 10, text = '6')
Six.bind("<Button-1>",six)

Seven = Button(MidFrame,height = 3, width = 10, text = '7')
Seven.bind("<Button-1>",seven)

Eight = Button(MidFrame,height = 3, width = 10, text = '8')
Eight.bind("<Button-1>",eight)

Nine = Button(MidFrame,height = 3, width = 10, text = '9')
Nine.bind("<Button-1>",nine)

Reset = Button(MidFrame, height = 3, width = 10, text= "Reset")
Reset.bind('<Button-1>',reset)

Advanced_Button = Button(MidFrame, height = 3, width = 10, text= "Advanced\nMode")
Advanced_Button.bind('<Button-1>',create_window)

#Button Definition
close= Button(BottomFrame,text="Close", command = quit)

add= Button(BottomFrame, height = 3, width = 10, text="Add\n+")
add.bind("<Button-1>",addition)

sub= Button(BottomFrame, height = 3, width = 10, text="Subtract\n-")
sub.bind("<Button-1>",subtract)

multi= Button(BottomFrame, height = 3, width = 10, text="Multiply\n*")
multi.bind("<Button-1>",multiply)

divi= Button(BottomFrame, height = 3, width = 10, text="Divide\n/")
divi.bind("<Button-1>",division)

equal = Button(BottomFrame, height = 3, width = 10, text= "EqualTo\n=")
equal.bind('<Button-1>',EqualTo)

#Packing
TopFrame.pack(side = TOP)
MidFrame.pack()
BottomFrame.pack(side= BOTTOM)
ScreenIn.pack(side= TOP,fill = X,padx=5,pady=10,ipady=3)

Zero.grid(row = 3, column = 1)
One.grid(row = 0, column = 0)
Two.grid(row = 0, column = 1)
Three.grid(row = 0, column = 2)
Four.grid(row = 1, column = 0)
Five.grid(row = 1, column = 1)
Six.grid(row = 1, column = 2)
Seven.grid(row = 2, column = 0)
Eight.grid(row = 2, column = 1)
Nine.grid(row = 2, column = 2)
Reset.grid(row=3, column=0)
Advanced_Button.grid(row=3, column=2)

close.pack(side= BOTTOM,fill = X);
add.pack(side = LEFT );
sub.pack(side = LEFT );
multi.pack(side = LEFT);
divi.pack(side = LEFT);
equal.pack(side= LEFT);

#Advanced Window
'''Functions'''

def Laplace_Transform(a,b,c):
    try:
        result = integrate(exp(a)*exp(-s*t),t)
        lim = lt(result) in range(0,inf)
        if result == sin(t):
            Laplace_Transform(sin(t),t,s)
        elif result == cos(t):
            Laplace_Transform(cos(t),t,s)
        elif result == tan(t):
            Laplace_Transform(tan(t),t,s)
    except:
        pass

def tFunc(event):
    global flag,expression
    if expression == '' or expression==0:
        expression = t
    else:
        expression = str(expression) +'*t'
    value_in_widget.set(expression)

def logFunc(event):
    global flag,expression
    expression = log(expression)
    value_in_widget.set(expression)

def sineFunc(event):
    global flag,expression
    expression = sin(value_in_widget.get())
    value_in_widget.set(expression)

def cosFunc(event):
    global flag,expression
    expression = cos(value_in_widget.get())
    value_in_widget.set(expression)

def tanFunc(event):
    global flag,expression
    expression = tan(value_in_widget.get())
    value_in_widget.set(expression)

def expFunc(event):
    global flag,expression
    expression = exp(value_in_widget.get())
    value_in_widget.set(expression)

def LaplaceFunc(event):
    global flag,expression
    expression = laplace_transform(expression,t,s)[0]
    value_in_widget.set(expression)

def IntegrateFunc(event):
    global flag,expression
    expression = integrate(expression,t)
    value_in_widget.set(expression)

def DifferentiateFunc(event):
    global flag,expression
    expression = diff(expression,t)
    value_in_widget.set(expression)

def PowerFunc(event):
    global flag,expression
    expression = str(expression) + '**'
    value_in_widget.set(expression)

'''Buttons'''
Button_t = Button(CentreFrame,height= 3, width = 10, text = 'var t')
Button_t.bind('<Button-1>',tFunc)
Button_log = Button(CentreFrame,height = 3, width=10, text = 'log')
Button_log.bind('<Button-1>',logFunc)
#Button_x = Button(CentreFrame,height= 3, width= 10, text = 'var x')
#Button_x.bind('<Button-1>',xFunc)
Button_sin = Button (CentreFrame,height=3 , width = 10, text = 'Sin')
Button_sin.bind('<Button-1>',sineFunc)
Button_cos = Button (CentreFrame,height=3, width = 10, text = 'Cos')
Button_cos.bind('<Button-1>',cosFunc)
Button_tan = Button(CentreFrame, height = 3, width = 10, text = 'Tan')
Button_tan.bind('<Button-1>',tanFunc)
Button_exp = Button(CentreFrame, height=3, width=10, text = 'e^')
Button_exp.bind('<Button-1>',expFunc)
Button_laplace = Button(CentreFrame,height =3 , width = 33, text = 'Laplace Transform\n(t -> s)')
Button_laplace.bind('<Button-1>',LaplaceFunc)
Button_integrate = Button (CentreFrame, height = 3, width = 10, text = 'Integrate\ndt')
Button_integrate.bind('<Button-1>',IntegrateFunc)
Button_differentiate= Button(CentreFrame, height =3 , width =10, text = 'Differentiate\ndt')
Button_differentiate.bind('<Button-1>',DifferentiateFunc)
Button_power= Button(CentreFrame,height =3 , width = 10 , text = 'Power')
Button_power.bind('<Button-1>',PowerFunc)

'''Packing'''
CentreFrame.pack(side= TOP)
Button_t.grid(row=0,column=0)
Button_log.grid(row=0,column=1)
Button_sin.grid(row=0,column=2)
Button_cos.grid(row=1,column=0)
Button_tan.grid(row=1,column=1)
Button_exp.grid(row=1,column=2)
Button_laplace.grid(row = 2, columnspan = 3)
Button_integrate.grid(row = 3, column=0)
Button_differentiate.grid(row=3, column=1)
Button_power.grid(row =3, column=2)
#/Advanced Windows

root.mainloop();
