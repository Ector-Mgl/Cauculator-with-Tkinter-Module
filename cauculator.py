from tkinter import *

colour_1 = '#e8af02'  # orange
colour_2 = '#ffffff'  # white
colour_3 = '#000000'  # black
colour_4 = '#999894'  # grey
colour_5 = '#3b3a39'  # dark grey


class button:
    def __init__(self, colour, tex='', weig=20, heig=20, back=colour_4, plaX=0, plaY=0, font_colou=colour_2, comma=None):
        self.colour = colour
        self.weig = weig
        self.heig = heig
        self.back = back
        self.plaX = plaX
        self.plaY = plaY
        self.tex = tex
        self.font_colou = font_colou
        self.comma= comma
    def create_button(self, name_variable):
        self.name_variable = name_variable
        name_variable = Button()
        name_variable.config(width=self.weig, height=self.heig, bg=self.back, text=(self.tex), fg=self.font_colou,
                             font=('arial', '10', 'bold'), relief=RAISED, overrelief=RIDGE, command=self.comma)
        name_variable.place(x=self.plaX, y=self.plaY)


app = Tk()
app.minsize(266, 430)
app.maxsize(266, 430)
app.config(background=colour_3)
app.title('Cauculator-ECTOR')


###################### Show in the Screen
variabl=  StringVar()
variabl.set('0.0')
all_values=''
def show_values(event):
    global all_values
    all_values += str(event)
    variabl.set(all_values)

def clear():
    variabl.set('0.0')
    global all_values
    all_values=''

def square_roots():                #Descobrir a raiz (in portuguese)
    global all_values
    all_values+= '**(1/2)'

def rest():
    global all_values
    all_values+= 0
#######################
#######################function to Cauculate
def cauculate():
    global all_values
    result= eval(all_values)
    variabl.set(result)




#######################

dude = Label(textvariable=variabl, width=20, height=5, font='arial 16 bold', anchor='e')
dude.place(x=0, y=0)


# top buttons
butf = button('trar', tex='AC', weig=7, heig=3, plaX=0, plaY=130, back=colour_4, comma= lambda : clear())
butf.create_button('jyyyf')

butg = button('trar', tex='+/-', weig=7, heig=3, plaX=66, plaY=130, back=colour_4, comma= lambda : square_roots())
butg.create_button('jygrrf')

buth = button('trar', tex='%', weig=7, heig=3, plaX=132, plaY=130, back=colour_4, comma= lambda : show_values('%'))
buth.create_button('jff')

butj = button('trar', tex='÷', weig=7, heig=3, plaX=198, plaY=130, back=colour_4, comma= lambda : show_values('/'))
butj.create_button('jff')

# Second column

but7 = button('trar', tex='7', weig=7, heig=3, plaX=0, plaY=190, back=colour_5, comma= lambda : show_values('7'))
but7.create_button('col7hd')
but8 = button('trar', tex='8', weig=7, heig=3, plaX=66, plaY=190, back=colour_5, comma= lambda : show_values('8'))
but8.create_button('cafwaeehd')
butd = button('trar', tex='X', weig=7, heig=3, plaX=198, plaY=190, back=colour_1, comma= lambda : show_values('*'))
butd.create_button('jkolof')
but9 = button('trar', tex='9', weig=7, heig=3, plaX=132, plaY=190, back=colour_5, comma= lambda : show_values('9'))
but9.create_button('cowqq')



# Third Colummn
but4 = button('trar', tex='4', weig=7, heig=3, plaX=0, plaY=250, back=colour_5, comma= lambda : show_values('4'))
but4.create_button('coawqhd')
but5 = button('trar', tex='5', weig=7, heig=3, plaX=66, plaY=250, back=colour_5, comma= lambda : show_values('5'))
but5.create_button('cor3hd')
but6 = button('trar', tex='6', weig=7, heig=3, plaX=132, plaY=250, back=colour_5, comma= lambda : show_values('6'))
but6.create_button('colfnd')
buts = button('trar', tex='-', weig=7, heig=3, plaX=198, plaY=250, back=colour_1, comma= lambda : show_values('-'))
buts.create_button('ff')

# Fourth column
but2 = button(colour='green', tex='2', weig=7, heig=3, plaX=66, plaY=310, back=colour_5, comma= lambda : show_values('2'))
but2.create_button('green_btn')
but1 = button('trar', tex='1', weig=7, heig=3, plaX=0, plaY=310, back=colour_5, comma= lambda : show_values('1'))
but1.create_button('colo4')
but3 = button('trar', tex='3', weig=7, heig=3, plaX=132, plaY=310, back=colour_5, comma= lambda : show_values('3'))
but3.create_button('col4hd')
buta = button('trar', tex='+', weig=7, heig=3, plaX=198, plaY=310, back=colour_1, comma= lambda : show_values('+'))
buta.create_button('jyff')

# Last column
but0 = button('oim', '0', 16, 3, back=colour_5, plaX=0, plaY=370, comma= lambda : show_values('0'))
but0.create_button('random2')
but11 = button('traer', tex='.', weig=7, heig=3, plaX=132, plaY=370, back=colour_5, comma= lambda : show_values('.'))
but11.create_button('cobbhd')
butw = button('trar', tex='=', weig=7, heig=3, plaX=198, plaY=370, back=colour_1, comma= lambda :cauculate())
butw.create_button('col4hd')





app.mainloop()
