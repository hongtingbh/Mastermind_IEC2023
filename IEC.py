import random
from tkinter import *
from tkinter import ttk
phase = "digits"
root = Tk()
root.geometry("800x500")

class Game:
  code= ""
  guess=""
  attempt = 1
  digits = -1
  dict = {
      "black": 0,
      "white": 0
  }
  def setDigits(self):
    #User decides number of digits for play
    if self.digits < 4 or self.digits > 6:
        warning.config(bg='#ff0000') # Red bg on instruction
        warning.configure(text=str(self.digits)+ " is not a valid entry. Enter 4-6.")
        return
        
    #Generate code
    for i in range(self.digits):
        self.code+=(str(random.randrange(0,10)))
    global phase 
    phase = "gameloop"
    label.configure(text="Please input your guess ("+str(self.digits)+" digits)")
    warning.config(bg='#F0F0F0') # Reset colour
    warning.configure(text="")
    attempt.configure(text="Attempt: " + str(game1.attempt))
  
  def guess_score(self):
    for i in range(len(self.code)):
        if self.code[i] == self.guess[i]: #Matching position and number
            self.dict["black"]+=1
        elif self.guess.find(self.code[i]) > -1: #Matching number but not position
            self.dict["white"]+=1
    # guess.configure(text=)
    

  def gameLoop(self):
    global phase
    self.dict["black"]=0 #Reset score
    self.dict["white"]=0

    if len(self.guess) != self.digits: # check # of digits guessed
        warning.configure(text=self.guess + " has "+str(len(self.guess))+
                            " digits. Input a "+str(self.digits)+" digit guess.")
        return
    self.guess_score() # Update black and white counters
    attempt.configure(text="Attempt: " + str(game1.attempt)) # Show attempt number
    counter.configure(text="Black: " + str(self.dict["black"])+ "\n White: " + str(self.dict["white"])) # Show score
    if self.dict["black"] == self.digits:
        warning.configure(text="Congratulations!")
        phase = "gameover"
        return
    else:
        warning.configure(text="Wrong!")
        self.dict["black"]=0 #Reset score
        self.dict["white"]=0
        self.attempt +=1
    if self.attempt > 10: #Attempt Limit
        warning.configure(text="You have reached "+str(self.attempt-1)+" attempts. You lose!\n" +
                          "The code is " + game1.code)
        phase = "gameover"

game1 = Game()

def get_data():
    global entry
    input = entry.get()
    print("Phase: ", phase)
    if phase == "digits":
        game1.digits = int(input)
        game1.setDigits()
    elif phase == "gameloop":
        game1.guess = input
        game1.gameLoop()
# Labels
label = Label(root, text="Please enter the # of digits to guess (4-6)", font=("Courier 22 bold"))
label.pack()
warning = Label(root, text="", font=("Courier 22 bold"))
warning.pack()
counter = Label(root, text="", font=("Courier 22 bold"))
counter.pack()
attempt = Label(root, text="", font=("Courier 22 bold"))
attempt.pack()
guess = Label(root, text="", font=("Courier 22 bold"))
guess.pack()

# Text box for user input
entry = Entry(root, width= 42)
entry.focus_set()
entry.pack()
# Button
ttk.Button(root, text="Enter", width= 20, command=get_data).pack(pady=20)

root.mainloop()