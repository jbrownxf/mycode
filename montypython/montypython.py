#!/usr/bin/env python3 
round = 0 # integer to begin building loop
while(True): #initaites the infite while loop
   round = round +1
   print('Finish the movie title, "Monty Python\'s The Life of ______"')
   answer = input() 
   if answer.lower() == 'brian':
      print('Correct')
      break
   if answer.lower() == 'shrubbery':
      print ('You gave the super secret answer!')
      break
   elif(round == 3):
      print('Sorry, the answer was Brian.')
      break
   else:
      print('Sorry. Try again.')
    