#!/usr/bin/env python3
#while statement to identify what networking standard the user is using

#while "np" is one of the explict options the user is will exit the script
while(True):
   np= input('What L2 protoccol are you using? ')
   
   if np.lower() == "eth" or np.lower() == "ethernet": #defined explicit variable
      print('ethernet allowed')
      break #break allow the user to quit the while loop after an explicit match 
   
   elif np.lower() == "fc": 
      print('fibre channel allowed')
      break

   elif np.lower() == 'ifb':
      print('infiniband allowed')
      break

   elif np.lower() == 'otn':
      print('optical network allowed')
      break

   else: #if an explicit match is not made loop is ran again
      print('No idea what that technology is')
      #returns to line 5
print('Enjoy your networking')