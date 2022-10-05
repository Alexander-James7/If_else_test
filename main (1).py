from random import *
a = randint(1, 6)

x = (int)(input("Guess a number between 1 and 6:"))

if x<a:
  print ("Too Low, the number is " + str(a))
if x>a:
  print ("Too high, the number is " +  str(a))
if x==a:
  print ("Corrrect, good job")

