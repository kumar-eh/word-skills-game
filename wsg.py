from tkinter import *
import random
import sys
import tkinter.messagebox
from tkinter.messagebox import *
lists = []
counter = 60
global e
global shuffled


# starting score is 0 #
Score = 0 

file = open('dictionaryWords.txt', 'r+')

root = Tk()

def counter_score(s):
    def counters():
        global Score
        s.config(text=str(Score))
        s.after(1000, counters)
    counters()


def three_letter(s):
    global Score
    Score += 5
    s.config(text=str(Score))


def four_letter(s):
    global Score
    Score += 10
    s.config(text=str(Score))


def five_letter(s):
    global Score
    Score += 20
    s.config(text=str(Score))


def six_letter(s):
    global Score
    Score += 100
    s.config(text=str(Score))

# when button b is clicked this is compiled #
def answer(e): 
    global l
    if len(e) < 3 or len(e) > 6:
        print(showwarning('Warning', 'Minimum number of letters should be three and maximum should be six'))
    else:
        if len(e) == 3:
            with open('dictionaryWords.txt', 'r') as read_obj:
                for line in read_obj:
                    if e.casefold() in line.casefold():
                        if e not in lists:
                            lists.append(e)
                            three_letter(s)
                            return
                        else:
                            print(showwarning("Alert" , "Word already entered"))
                            return

        if len(e) == 4:
            with open('dictionaryWords.txt', 'r') as read_obj:
                for line in read_obj:
                    if e.casefold() in line.casefold():
                        if e not in lists:
                            lists.append(e)
                            four_letter(s)
                            return
                        else:
                            print(showwarning("Alert" , "Word already entered"))
                            return

                        


        if len(e) == 5:
            with open('dictionaryWords.txt', 'r') as read_obj:
                for line in read_obj:
                    if e.casefold() in line.casefold():
                        if e not in lists:
                            lists.append(e)
                            five_letter(s)
                            return
                        else:
                            print(showwarning("Alert" , "Word already entered"))
                            return



        if len(e) == 6:
            with open('dictionaryWords.txt', 'r') as read_obj:
                for line in read_obj:
                    if e.casefold() in line.casefold():
                        if e not in lists:
                            lists.append(e)
                            six_letter(s)
                            return
                        else:
                            print(showwarning("ALert" , "Word already entered"))
                            return


        else:
            print(showwarning('Warning', 'Please enter a correct word'))
            return



def counter_label(timer):
    def count():
        global counter
        global Score
        if(counter > 0):
            counter-=1
            timer.config(text=str(counter))
            timer.after(1000, count)

        else:
            result = tkinter.messagebox.showinfo("Game over","Press yes to exit")
            if(result == True):
                root.destroy()
            else:
                root.destroy()         
    count()

    
# for choosing a random a six letter word form the file#
def question(word):  
    while True:
        words = random.choice(open('dictionaryWords.txt').read().split()).strip()
        if len(words) == 6:
            shuffled = list(words)
            random.shuffle(shuffled)
            shuffled = ''.join(shuffled)
            word.config(text=str.upper(shuffled))
            break

# score label#
l = Label(root, text='Score')  
l.pack(side='top')


# label for changing score#
s = Label(root, text=Score)  
s.pack()
counter_score(s)

root.title('Game')

c = Canvas(root, height=600, width=400)
c.pack()


# timer widget#
timer = Label(root, fg='green' , font = ("Helvetica", 25))  
timer.pack()
counter_label(timer)


# frame within the canvas#
f = Frame(root, bg='#03dac5')  
f.place(relx=0.10, rely=0.10, relwidth=0.8, relheight=0.8)


# USER ENTRIED WORD#
e = Entry(f, bg='#3da4f2')  
e.place(relx=0.5, rely=0.10, relheight=0.10, relwidth=0.4, anchor='n')


# for entering after typing the word#
b = Button(f, bg='#ff0000', text='Submit', command=lambda : answer(e.get()))  
b.pack(side='bottom')


# for displaying the six letter word#
word = Label(f, bg='#3da4f2' , fg = "#ffffff")  
word.place(relx=0.5, rely=0.9, relheight=0.10, relwidth=0.4, anchor='s')
question(word)

root.mainloop()
