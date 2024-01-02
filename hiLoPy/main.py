import game_data as gd
import random as rn
flag = False
lives =3
print("Welcome to Higher or Lower game!!")
while(flag != True or lives <= 0):
  print(f"You have {lives} lives")
  first = gd.data[rn.randint(0,len(gd.data)-1)]
  second = gd.data[rn.randint(0,len(gd.data)-1)]

  if(first == second):
    second = gd.data[rn.randint(0,len(gd.data)-1)]

  print(f" Is {first['name']} is higher than {second['name']}")
   
  answer = input("Enter h for higher and l for lower: ") 
  if(answer == 'h'):
    if(first['follower_count'] >= second['follower_count']):
      print("You are correct")
      second = gd.data[rn.randint(0,len(gd.data)-1)]
    else:
      print("You are wrong")
      lives -= 1
      
  elif(answer == 'l'):
    if(first['follower_count'] < second['follower_count']):
      print("You are correct")
      second = gd.data[rn.randint(0,len(gd.data)-1)]
    else:
      print("You are wrong")
      lives -= 1
      first = gd.data[rn.randint(0,len(gd.data)-1)]
      second = gd.data[rn.randint(0,len(gd.data)-1)]
  else:
    print("Invalid input")
    continue
  print(f"The next question is {first['name']} higher than {second['name']}")
  answer = input("Enter y to continue or n to exit: ")
  if(answer == 'y'):
    continue
  else:
    flag = True
    print("Thanks for playing")
  
  
  