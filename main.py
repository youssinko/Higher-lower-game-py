from game_data import data
import random
from art import logo, vs
score=0
games=True
new= random.choice(data)
while games:
  new1=new
  new1=random.choice(data)
  #regenerate new random if A and B are the same.
  if new == new1:
    new1=random.choice(data)
  count=new['follower_count']
  print(count)
  count1=new1['follower_count']
  print(count1)
  


  def definition(account):
    name=account['name']
    description=account['description']
    country=account['country']
    return(f'{name} {description} from {country}')
    
  print(f'{logo} {definition(new)} {vs} {definition(new1)}')
  
  guess=input("A or B ?\n").lower()
  
  def game(guess,count,count1):
    if count > count1:
      return guess == 'a'
    else:
      return guess == 'b'
  is_correct=game(guess,count,count1)
 
  if is_correct:
    score+=1
    print(f'you won, score:{score}')
  else:
    games=False
    print(f'you lost, score:{score}')
