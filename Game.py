#python 3.7.1
import random
print("☆☆☆☆☆☆☆☆☆☆☆  Snake Water Gun Game  ☆☆☆☆☆☆☆☆☆☆☆")
lives=10
number_of_lives=0
name=input("Please enter your name: ")
np=0
cp=0
lst=['s','w','g']
print("enter s for snake\nenter w for water\nenter g for gun")
while number_of_lives<lives:
  number_of_lives=number_of_lives+1
  print("enter your choice ")
  choice=input()
  com=random.choice(lst)
  print(f"{name} use {number_of_lives} lives")
  def li():
      print("----------------------")
  if choice==com:
    print("tie both get 1 points")
    li()
  elif choice=="s"and com=="g":
    print(f"{name} get 1 point \ncomputer choose w")
    li()
    np=np+1
  elif choice=="s"and com=="w":
    print(f"{name} lose \ncomputer get 1 point computer choose g")
    li()
    cp=cp+1
  elif choice=="w"and com=="g":
    print(f"{name} get 1 point \ncomputer choose g")
    li()
    np=np+1
  elif choice=="w"and com=="s":
    print(f"{name} lose \ncomputer get 1 point computer choose s")
    li()
    cp=cp+1
  elif choice=="g"and com=="s":
    print(f"{name} get 1 point\n computer choose s")
    li()
    np=np+1
  elif choice=="g"and com=="w":
    print(f"{name} lose \ncomputer get 1 point computer choose w")
    li()
    cp=cp+1
  else:
    print("invalid input")
    li()
print("~~~~~~~~~~~~~~~~~~ Points Table ~~~~~~~~~~~~~~~~")
print(f"computer points {cp}")
print("••••••••••••••••••••••••••••••••••••••")
print(f"{name} points {np}")
print("••••••••••••••••••••••••••••••••••••••")
print("                           WINNER IS                              \n")
if cp>np:
  print("                         COMPUTER ")
elif np>cp:
  print(f"                        {name} ")
else:
  print("                          tie")
#This code is written by Nirav Prajapati
