# print("welcome to the rollercoaster")
# height = int(input("How tall are you in cm"))
# bill = 0
#
# if height >= 120:
#     print("You can ride the rollercoaster! ")
#     age = int(input("How old are you? "))
#     if age < 12:
#         bill = 5
#         print("Please pay $5")
#     elif age <=18:
#         bill = 7
#         print("Please pay $7")
#     else:
#         bill = 12
#         print("Please pay $12")
#
# wants_photo =input("Do you want a photo taken? Y or N")
# if wants_photo == "Y":
#     bill +=3
#     print(f"your bill is: ${bill}")
#
# else:
#     print("sorry,you have to grow taller before you can ride")
# number = int(input("Which number do you want to change"))
# if number % 2==0:
#     print("number is even")
# else:
#     print("number is odd")
# height = float(input("your height in m:"))
# weight = float(input("your weight in kg:"))
#
# bmi = round(weight / height ** 2)
# if bmi < 18.5:
#     print(f"your bmi is {bmi},You are underweight")
# elif bmi < 25:
#     print(f"your bmi is {bmi},You have a normal weight")
# elif bmi< 30:
#     print(f"your bmi is {bmi},You are overweight")
# elif bmi < 35:
#     print(f"your bmi is {bmi},You are obese")
# else:
#     print(f"your bmi is {bmi},You are clinically obese")
# year = int(input("Which year you want to check?\n"))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("leap year")
#         else:
#             print("not leap year")
#     else:
#         print("leap year")
# else:
#         print("not leap year")
# print("welcome to Mesazz pizzariya")
# size = input("what size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni?")
# extra_cheese = input("Do you want extra cheese?")
# bill = 0
#
# if size == "S":
#         bill += 15
# elif size == "M":
#         bill += 20
# else:
#         bill += 25
# if add_pepperoni == "Y" :
#     if size == "S":
#         bill += 2
#     else :
#         bill += 3
# if extra_cheese == "Y" :
#     bill += 1
#     print(f"your final bill is ${bill}")

print("welcome to Treasure Island")
print("Your mission is to find the treasure")
choice1 = input('Your\'re at a cross road, where do you want to go ? type "Left" or "right".\n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake.there is an island in the middle of the lake. "wait" to wait for a boat.Type "swim"'
          'to swim across.\n').lower()
  if choice2 == "wait":
    choice3 = input( "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
    if choice3 == "red":
     print("It's a room full of fire.Game Over")
    elif choice3 =="yellow":
      print("Yoy found the treasure! you win")
    elif choice3 == "blue":
        print("You enter a room of beasts. Game Over")
    else:
        print("You choose a door that doesn't exits.Game Over")
  else:
    print("You got attacked by an angry trout. Game Over.")
else:
  print("you fell into a hole!Game Over")