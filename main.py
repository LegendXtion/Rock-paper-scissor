from tkinter import *
import random

#Windows Configuration
window= Tk()
window.title("Rock, Paper, Scissor")
window.resizable(False, False)
# window.geometry("400x300")

#Variables
User_Score = 0
Computer_Score = 0
User_Choice = ''
Computer_Choice = ''
choices = ['rock', 'paper', 'scissor']

#Functions
def rock():
	global User_Choice, Computer_Choice, choices
	User_Choice = 'rock'
	Computer_Choice = random.choice(choices)
	result(User_Choice, Computer_Choice)

def paper():
	global User_Choice, Computer_Choice, choices
	User_Choice = 'paper'
	Computer_Choice = random.choice(choices)
	result(User_Choice, Computer_Choice)
	
def scissor():
	global User_Choice, Computer_Choice, choices
	User_Choice = 'scissor'
	Computer_Choice = random.choice(choices)
	result(User_Choice, Computer_Choice)

def result(user_choice, computer_choice):
	global User_Score, Computer_Score

	if user_choice == computer_choice:
		winner = 'Tie'
	elif user_choice=='rock' and computer_choice=='scissor':
		winner = 'You'
		User_Score+=1
	elif user_choice=='scissor' and computer_choice=='paper':
		winner = 'You'
		User_Score+=1
	elif user_choice=='paper' and computer_choice=='rock':
		winner = 'You'
		User_Score+=1
	elif computer_choice=='rock' and user_choice=='scissor':
		winner = 'Computer'
		Computer_Score+=1
	elif computer_choice=='scissor' and user_choice=='paper':
		winner = 'Computer'
		Computer_Score+=1
	elif computer_choice=='paper' and user_choice=='rock':
		winner = 'Computer'
		Computer_Score+=1

	statement = "-"*20+f'\nYour Choice : {user_choice.upper()}'+f'\nComputer Choice : {computer_choice.upper()}'+f'\nResult : {winner}\n'+'-'*20+'\n'*7
	textarea.insert(END, statement)
	textarea.see("end")
	score1.config(state='normal')
	score2.config(state='normal')
	score2.delete("1.0", END)
	score1.delete("1.0", END)
	score1.insert(END, User_Score)
	score2.insert(END, Computer_Score)
	score1.config(state='disabled')
	score2.config(state='disabled')

#Widget Configuration
score1 = Text(master=window, width=5,  height=1, state='disabled')  
score1.grid(row=2, column=1, rowspan=2)

Label(master=window, text="You", font="Times 16").grid(row=1, column=1)
Label(master=window, text='PC', font="Times 16").grid(row=1, column=3)

button1 = Button(master=window, text="Rock", bg="skyblue", width=30, command=rock)
button1.grid(row=1, column=2)

score2 = Text(master=window, width=5,  height=1, state='disabled')  
score2.grid(row=2, column=3, rowspan=2)

button2 = Button(master=window, text="Paper", bg="pink",width=30, command=paper)
button2.grid(row=2, column=2)

button3 = Button(master=window, text="Scissor", bg="skyblue", width=30, command=scissor)
button3.grid(row=3, column=2)

textarea = Text(master=window, width=30, height=12, bg="green", font="times 16", fg='white')
textarea.grid(row=4, column=1, columnspan=3)

#Mainloooooooooooop
window.mainloop()
