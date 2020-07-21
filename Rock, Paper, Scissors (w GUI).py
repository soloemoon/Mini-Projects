from random import randint
from tkinter import *

''' Simple Rock, Paper, Scissors game'''
play_options = ['Rock', 'Paper', 'Scissors']

outcomes = ['Tie', 'Sorry, You Lose', 'You Win!!!']

computer = play_options[randint(0,2)] # Randomize selection

def dropdown_change(*args):
    human = tkvar.get()
    return human
    
def move():
       
        human = tkvar.get()
        computer = play_options[randint(0,2)]
        
        if human == computer:
            outcome = outcomes[0]
            
        elif human == play_options[0] and computer == play_options[1]:
            outcome = outcomes[1]
            
        elif human == play_options[1] and computer == play_options [2]:
            outcome = outcomes[1]
            
        elif human == play_options[2] and computer == play_options[0]:
            outcome = outcomes[1]
            
        else:
            outcome = outcomes[2]  
            
        computer_entry.config(state=NORMAL)
        computer_entry.delete(0, END)
        computer_entry.insert(0, str(computer))
        
        outcome_entry.config(state=NORMAL)
        outcome_entry.delete(0, END)
        outcome_entry.insert(0, str(outcome))
        
        computer_entry.config(state='readonly')
        outcome_entry.config(state = 'readonly')
                   
root = Tk()
root.title('Rock, Paper, Scissors')

# Define dropdown
Label(root, text = 'Select Play').grid(row = 0, column = 0)
tkvar = StringVar(root)
tkvar.trace('w', dropdown_change)
player_menu = OptionMenu(root, tkvar, *play_options)
player_menu.grid(row = 0, column =1)

# Define Entry Boxes
Label(root, text = "Computer's Move").grid(row = 1, column = 0)
computer_entry = Entry(root, state = 'readonly')
computer_entry.grid(row = 1, column = 1)

Label(root, text = 'Outcome').grid(row = 2, column = 0)
outcome_entry = Entry(root, state='readonly')
outcome_entry.grid(row = 2, column = 1)


play_button = Button(root, text = 'Play', command = move).grid(row = 3, column = 0)
quit_button = Button(root, text = 'Quit', command = root.destroy).grid(row =3, column = 1)

root.mainloop()

    
        
    
        
