#States changing variables
min=0
max=1001
print("Hello I am a number wizard, I will guess your number. Tell me if I get it right!")
print("Think of a number between 1 and 1000 tell me if my guess is lower or higher by entering l, or h. If I get it right hit c.")
guess=500
print("Is your number higher, lower, or equal to than " + str(guess))
while(1):
#Checks for what the value of  users number is
  check = input()
  if(check == "h" or check == "H"):
    min = guess
    guess = round((min + max)/2)
    print("Is your number higher, lower, or equal to than than " + str(guess))
  elif(check == "l" or check == "L"):
    max = guess
    guess = round((min + max)/2)
    print("Is your number higher, lower, or equal to than " + str(guess))
  elif(check == "e" or check == "E"):
    print("Told you I was a number wizard!")
    break
  #Results if the user doesn't type what was requested
  else:
    print("Please type something I understand.")
