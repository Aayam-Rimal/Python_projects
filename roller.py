#die roller program
import random
print("--dice roller program--")

while True:

 try:
  number_of_rolls= int(input("enter how many dice you want to roll: "))
  number_of_sides= int(input("enter how many sided dice you want to roll: "))

  print(f"rolling {number_of_rolls} dice with {number_of_sides} side each:")
  die_result=[]

  for i in range(number_of_rolls):
    result=random.randint(1,number_of_sides)
    die_result.append(result)

  print("result:",die_result)

  sum_of_result=sum(die_result)
  print("total:",sum_of_result)

  average= sum_of_result/len(die_result)
  print("the average is :",average)

  highest= max(die_result)
  print("the highest number rolled is:",highest)

  lowest= min(die_result)
  print("the lowest number rolled is: ",lowest)

  choice=input("do you want to continue? (y/n)")
  if choice=="y":
   continue
  elif choice=="n":
   break

 except ValueError:
  print("error!! enter a integer!")
