from tkinter import *
import random
import sys
from tkinter.messagebox import *

counter = 60                                                                                                            #for time#



global e

Score =0                                                                                                                #starting score is 0#

file = open("files.txt" , "r+")

root = Tk()


def repeat_words():
    

        else:
            print(showwarning("alert" , "Word already entered"))
    

def counter_score(s):
    def counters():
        global Score
        s.config(text=str(Score))
        s.after(1000, counters)
    counters()




def three_letter(s):
    global Score
    Score+=5
    s.config(text = str(Score))



def four_letter(s):
    global Score
    Score+=10
    s.config(text = str(Score))


    
def five_letter(s):
    global Score
    Score+=20
    s.config(text = str(Score))



def six_letter(s):
    global Score
    Score+=100
    s.config(text = str(Score))







def answer(e):                                                                                                           #when button b is clicked this is compiled#
    l= [] 
    global Score
    global words
    if(len(e) <3 or len(e) > 6):
        print(showwarning("Warning" , "Minimum number of letters should be three and maximum should be six"))
    else:
        if(len(e) == 3):
            with open("files.txt", "r") as read_obj:
                for line in read_obj:
                    if e.casefold() in line.casefold():
                        repeat_words()
                        three_letter(s)


                   
        if(len(e) == 4):
            with open("files.txt", "r") as read_obj:
                for line in read_obj:
                    if e.casefold() in line.casefold():
                        four_letter(s)
                        return


                
        if(len(e) == 5):
            with open("files.txt", "r") as read_obj:
                for line in read_obj:
                    if e.casefold() in line.casefold():
                        five_letter(s)
                        return


                
        if(len(e) == 6):
            with open("files.txt", "r") as read_obj:
                for line in read_obj:
                    if e.casefold() in line.casefold():
                        six_letter(s)
                        return
        else:
            print(showwarning("Warning" , "Please enter a correct word"))
            return
            



def counter_label(timer):                                                                                               #for timer function definition#
  def count():
    global counter
    counter -= 1
    timer.config(text=str(counter))
    timer.after(1000, count)
  count()



def question(word):                                                                                                     #for choosing a random a six letter word form the file#
    while(True):
        words = random.choice(open("filen.txt").read().split()).strip()
        if(len(words) == 6):
            shuffled = list(words)
            random.shuffle(shuffled)
            shuffled = ''.join(shuffled)
            word.config(text = str.upper(shuffled))
            break


        
l = Label(root , text = "Score")                                                                                        #score label#
l.pack(side = "top")


s = Label(root , text =Score)                                                                                           #label for changing score#
s.pack()
counter_score(s)


root.title("Game")



c = Canvas(root , height = 600 , width = 400)
c.pack()

timer = Label(root, fg="green")                                                                                         #timer widget#
timer.pack()
counter_label(timer)


f  = Frame(root , bg = "#4eedd3")                                                                                       #frame within the canvas#
f.place(relx = 0.1 , rely = 0.1 , relwidth = 0.8 , relheight = 0.8)


e = Entry(f , bg = "#3da4f2")                                                                                           #USER ENTRIED WORD#
e.place(relx = 0.5 , rely = 0.1 , relheight = 0.10 , relwidth = 0.4 , anchor = "n")



b = Button(f , bg = '#ff0000' , text = "Submit"  , command = lambda : answer(e.get()))                                  #for entering after typing the word#
b.pack(side = "bottom")





word = Label(f , bg = "#3da4f2")                                                                                        #for displaying the six letter word#
word.place(relx = 0.5 , rely = 0.9 , relheight = 0.10 , relwidth = 0.4 , anchor = "s")
question(word)




root.mainloop()
