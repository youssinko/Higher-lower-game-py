from game_data import data
import random
from art import logo, vs
score=0
new= random.choice(data)
new1=random.choice(data)
print(f"{logo}\nChoice A: {new['name']} {new['description']} from {new['country']}\n {vs} \n Choice B: {new1['name']} {new1['description']} from {new1['country']}")
output=input("A or B ?\n").lower()
if output == "a":
   a= new
else:
   b= new1
print(new['follower_count'])
print(new1['follower_count'])

if new['follower_count'] > new1['follower_count'] and output =="a":
  score+=1
  print(f"you won! {score}")
elif new['follower_count'] < new1['follower_count'] and output =="b":
  score+=1
  print(f"you won! {score}")
else:
  print(f"you lost! {score}")