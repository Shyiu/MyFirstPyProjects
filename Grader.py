grade = float(input("What is your grade?"))

if(grade >= 90):
  print('This is an "A"')
elif(grade >= 80 and grade <90):
  print('This is a "B"')
elif(grade >= 70 and grade < 80):
  print('This is a "C"')
elif(grade >= 60 and grade < 70):
  print('This is a "D"')
elif(grade < 60):
  print('This is a "F"')
else:
  print("Please type something I understand")
