# Edwin Zeng
# This program will simulate chopsticks. It includes features such as split, attack, restart game, select the number of players, select initial finger count, and more. 
import time
username_tracker = []
hand_tracker = []
out_list = []
left_right = ["l","r"]
current_player = 1
num_of_players = 0
counter = 0

def reset_game():
  global username_tracker, hand_tracker, current_player, num_of_players
  username_tracker.clear()
  hand_tracker.clear()
  out_list.clear()
  current_player = 1
  counter = 0
  print("Game restarted")
  main()

def get_input(prompt):
  response = input(prompt)
  if response.lower() == 'restart':
    reset_game()
  return response

def rules():
  while True: 
    know = get_input("Press y to continue with rules, press n to skip: ")
    if know == "y":
      print("RULES\n- Both players start with a set amount of fingers to begin with. \n- Each turn, a player will attack or split.\n- If a player attacks, they will choose, if possible, a hand to attack with, a person to attack, and a hand to attack.\n- Example: if someone attacks with their left hand which contains 2 fingers up an opponent's right hand which contains 1 finger up the opponent's right hand will now have 3 fingers up.\n- If one chooses to split, they will split the total between their hands.\n- Example: if someone has 3 in their left hand and 2 in their right hand they can split the total into 1 and 4.\n- If someone has 5 fingers up it turns into 0 and anything greater than 5 will end up being 0 + amount greater than 5.\n- If someone has 0 in both hands, they are out.\nLast person standing wins.\n")
      break
    elif know == "n":
      break
    else:
      print("Invalid input")
      continue
def player_count():
  global num_of_players
  while True:
    try: 
      num_of_players = int(get_input("Enter the number of players: "))
      if num_of_players <= 1:
        print("You need more than one player")
        continue
      else: 
        for i in range(num_of_players*2):
          hand_tracker.append(0)
        for i in range(num_of_players):
          out_list.append(0)
          username_tracker.append("Player "+str(i+1))
        break
    except ValueError:
      print("Please enter an integer")
      continue
      
def usernames():
  global num_of_players, name_option
  while True:
      name_option = get_input("Do you want to customize usernames? (y/n) ").lower()
      if name_option == "y":
          for num in range(num_of_players):
              while True:
                username = get_input(f"Player {num + 1}, enter your username: ")
                try: 
                  username = int(username)
                  if username >= 1 and username <= num_of_players:
                    print(f"Username cannot be the integers from 1 - {num_of_players}")
                    continue
                  else:
                    break
                except ValueError:
                  if username in username_tracker:
                    print("Username already taken")
                    continue
                  else:
                      username_tracker[num] = username
                      break
          break
      elif name_option == "n":
          break
      else:
          print("Please enter y or n.")
          continue
def finger_count():
  while True:
    try: 
      initial_finger = int(get_input("How many fingers do you want to start with on each hand? "))
      if initial_finger <= 0:
        print("Please enter a positive number")
        continue
      elif initial_finger >= 5:
        print("Initial cannot be greater than 4")
        continue
      else: 
        break
    except ValueError:
      print("Please enter an integer")
      continue
  for i in range(num_of_players*2):
    hand_tracker[i] = initial_finger

def split():
  global current_player
  added_together = hand_tracker[(current_player-1)*2] + hand_tracker[(current_player-1)*2+1]
  while True:
    try: 
      splits = int(get_input(f"Your left has {hand_tracker[(current_player-1)*2]} and your right has {hand_tracker[(current_player-1)*2+1]}. How many do you want your left to have? "))
      if splits < 0 or splits > added_together:
        print(f"Please enter a positive number that is less than or equal to the {added_together}")
        continue
      else:
        break
    except ValueError:
      print(f"Please enter valid integers to split the {added_together}")
      continue
  hand_tracker[(current_player-1)*2] = splits
  hand_tracker[(current_player-1)*2+1] = added_together - splits
  if hand_tracker[(current_player-1)*2+1] >= 5:
    hand_tracker[(current_player-1)*2+1] = hand_tracker[(current_player-1)*2+1] - 5
  if hand_tracker[(current_player-1)*2] >= 5:
    hand_tracker[(current_player-1)*2] = hand_tracker[(current_player-1)*2] - 5
  print(f"Your left now has {hand_tracker[(current_player-1)*2]} and your right has {hand_tracker[(current_player-1)*2+1]}.")
  
def move():
  global current_player, counter, num_of_players
  while hand_tracker[(current_player-1)*2]!= 0 or hand_tracker[(current_player-1)*2+1]!= 0:
    move_split_attack = get_input(f"{username_tracker[current_player-1]}, do you want to split (s) or attack (a)? (s/a) ").lower()
    if move_split_attack == "s":
      split()
      break
    elif move_split_attack == "a":
      attack_move()
      break
    else: 
      print("Please enter s or a. ")
      continue
  counter = 0
  for i in range(num_of_players):
    if hand_tracker[(i*2)] == 0 and hand_tracker[(i*2)+1] == 0:
      counter+=1
      out_list[i] = 1
    if hand_tracker[(current_player-1)*2]!= 0 or hand_tracker[(current_player-1)*2+1]!= 0:
      print(f"{username_tracker[i]}  LH: {hand_tracker[i*2]}  RH: {hand_tracker[i*2+1]}")
  if current_player == num_of_players:
    current_player = 0
    
def main():
  global current_player, counter, num_of_players
  print("Hello! This simulates the chopsticks game. Type restart at any time to restart the game from the beginning.")
  time.sleep(1)
  rules()
  player_count()
  usernames()
  finger_count()
  while True:
    move()
    if counter == num_of_players-1:
      print(f"{username_tracker[out_list.index(0)]} wins!")
      play_again = get_input("Do you want to play again? Type restart to play again and anything else to quit. ")
      if play_again.lower() != "restart":
        break
    current_player+=1

def attack_move():
  global current_player, num_of_players, username_tracker, name_option,counter, opponent_player
  
  while True:
    if hand_tracker[(current_player-1)*2] == 0:
      attack_hand = "r"
      break
    elif hand_tracker[(current_player-1)*2+1] == 0:
      attack_hand = "l"
    else: 
      attack_hand = get_input("Do you want to attack with your left or right hand? (l/r) ").lower()
      if attack_hand in left_right:
        break
      else:
        print("Please type l or r")
        continue
  while True:
    if counter == num_of_players-2:
      for num in range(num_of_players):
        if out_list[num] == 0 and num!= current_player-1:
          opponent_player = num+1
      break
    elif counter != num_of_players-2 and name_option == "y":
      opponent_player = get_input("Who do you want to attack? List their player number or username ")
    elif counter!= num_of_players-2 and name_option =="n": 
      opponent_player = get_input("Who do you want to attack? List their player number ")
    try: 
      opponent_player = int(opponent_player)
      if opponent_player > num_of_players or opponent_player < 1:
        print(f"Please enter a valid player number. There are {num_of_players} players.")
        continue
      elif opponent_player == current_player:
        print("You cannot attack yourself")
        continue
      else: 
        if out_list[opponent_player-1] == 1:
          print("This player has already been eliminated")
          continue
        else: 
          break
    except ValueError:
      if opponent_player not in username_tracker:
        print("Invalid username. Note this is case sensitive. ")
        continue
      elif username_tracker.index(opponent_player) == current_player-1:
        print("You cannot attack yourself!!!")
        continue
      else:
        opponent_player = username_tracker.index(opponent_player)+1
        if out_list[opponent_player-1] == 1:
          print("This player has already been eliminated")
          continue
        else:
          break
  while True: 
    opponent_hand = get_input("Do you want to attack the left or right hand? (l/r) ").lower()
    if opponent_hand in left_right:
      break
    else:
      print("Please type l or r")
      continue
  hand_tracker[(opponent_player-1)*2+left_right.index(opponent_hand)] +=   hand_tracker[(current_player-1)*2+left_right.index(attack_hand)]
  if hand_tracker[(opponent_player-1)*2+left_right.index(opponent_hand)] >= 5:
    hand_tracker[(opponent_player-1)*2+left_right.index(opponent_hand)] -=5
  if hand_tracker[(opponent_player-1)*2] == 0 and hand_tracker[(opponent_player-1)*2+1] == 0:
    print(f"{username_tracker[opponent_player-1]} is now out!")
main()
  