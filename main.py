
import art
import random
from replit import clear

def deal_card():
 cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
 card=random.choice(cards)
  return card

def calculate_score(cards):
  total=sum(cards)
  if total==21 and len(cards)==2:
    return 0
  if total>21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
    total=sum(cards)
  return total

def compare(user_score,comp_score):
  if user_score==comp_score:
    return "Draw"
  elif user_score==21 :
    return "you win"
  elif comp_score==21 :
    return "you lose"
  elif comp_score>21:
    return "you win"
  elif user_score>21:
    return "you lose"
  else:
    if user_score>comp_score:
      return "you win"
    else:
      return "you lose"
def play_game():
  print(art.logo)
  user_cards=[]
  computer_cards=[]
  is_game_over=False
  comp_score = 0
  user_score = 0
  
  for i in range(2):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())
    
  while not is_game_over:
    user_score=calculate_score(user_cards)
    comp_score=calculate_score(computer_cards)
    
    print(f"your cards : {user_cards} and your score : {user_score}")
    print(f"computers 1st card : {computer_cards[0]}")
    
    if user_score==0 or comp_score==0 or user_score>21:
      is_game_over=True
    else:
      
      user_should_deal=input("type y to draw another card or else n")
      if user_should_deal=="n":
        is_game_over=True
      else:
        user_cards.append(deal_card())
  
  while comp_score != 0 and comp_score < 17:
    computer_cards.append(deal_card())
    comp_score=calculate_score(computer_cards)
  print(f"your cards: {user_cards} and your final score {user_score}") 
  print(f"computers cards : {computer_cards} and computers score : {comp_score}")
     
  print(compare(user_score,comp_score))  
  
a=input("Do you want to play a game of blackjack : y or n")

if a=="y":
  clear()
  play_game()

restart=input("enter y to restart the game or else n")
while restart=="y":
  clear()
  play_game()
  
