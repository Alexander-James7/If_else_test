from random import *
a = randint(1, 6)
# this line generates a random number from 1 to 6

x = (int)(input("Guess a number between 1 and 6:"))
# this line asks the user to guess an integer from 1 to 6

if x<a:
  print ("Too Low, the number is " + str(a))
# this line tells the user that their number is too low, and gives them the correct answer
if x>a:
  print ("Too high, the number is " +  str(a))
# this line tells the user that their number is too high, and gives them the correct answer
if x==a:
  print ("Corrrect, good job")
# This line tells the user that their guess is correct
