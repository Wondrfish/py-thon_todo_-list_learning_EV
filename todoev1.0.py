import datetime
from time import sleep
from tqdm import tqdm
import random
import pyfiglet
import os



today = datetime.date.today()

todos = {}

class Gamemodes:
  def __init__(self, name, modes):
        self.name = name       # Sets the name of the game
        self.modes = modes     # Sets the modes for the game
   
  def display_modes(self):
      print(f"Available modes for {self.name}: {', '.join(self.modes)}")

positives = ["yeah", "yes", "shut down", "y"]
negatives = ["no", "nope", "nah", "n", "no way jose"]
close_out = ("close", "exit", "quit")


def tic_tac_toe(mode):
  print("tic tac toe not done yet")
  backhome()

def mine_sweeper(mode):
  print("mine sweeper not done yet")
  backhome()

def chess(mode):
  print("chess not done yet")
  backhome()

def backhome():
  print("\n back to menu \n")
  menu()

def keep_playing(reroll,gamemodes, mode):
  if reroll:
    print("\nplay again\n")
    gamesandmodes[mode](mode)
  else:
    print("\nbye")
    menu()

def menu():
  while True:
    print(f"Today is {today}")
    task = input("\nWhat Are we doing today \n\n 1)Task manager \n 2)calculator \n 3) file cleaner \n 4) games \n")
    if task == "1":
      choice()
    elif task == "2":
      print("calc not done yet")
      #calculator()
    elif task == "3":
      print("file cleaner not done yet")
      #file_cleaner()
    elif task == "4":
      games()
    elif task in close_out:
      print("bye")
      exit()
    else:
      print("invalid input try again")     


def games():
  pick_a_game = input("\nwhat do you wanna play \n 1)tic tac toe \n 2) mine sweeper \n 3) chess \n 4)dice    \n").strip()


  while pick_a_game not in gamesandmodes and pick_a_game not in close_out:
    print(f"\n'{pick_a_game}' was not a choice.")
    pick_a_game = input("\nChoose again: ").lower().strip()

  if pick_a_game in close_out:
    print("bye")
    exit()
  
  elif pick_a_game not in gamesandmodes:
    print(" no you must pick a game")
    return games()


  mode = input(f"\n You picked {pick_a_game}\n are you playing solo or vs mode\n").lower().strip()

  valid_modes = {mode for game in gamesandmodes.values() for mode in game["modes"]}

  while mode not in valid_modes:
    print(f"\n'{mode}' is not a valid mode.")
    mode = input("\nChoose solo or vs mode: ").lower().strip()

  print(f"\nOpening {pick_a_game} in {mode} mode...")
  for i in tqdm(range(10)):  # sim loading
      sleep(0.5)
  print(f"\n {pick_a_game} in {mode} is ready enjoy")
  gamesandmodes[pick_a_game]["function"](mode)


def dice_roll(num_dice):
   whaturolled = [random.randint(1,8) for i in range(num_dice)]
   return whaturolled

def dice(mode):
  print("\n RULES \n 7 is a insta win 2,4,8 mean you lose else roll again")
  try:
    num_dice = int(input("\n how many dice do u want \n"))
    if num_dice < 1:
      print("\n invalid input must be at least 1")
      return dice(mode)
  except ValueError:
    print("\n invalid input must be a number")
    
    return dice(mode)

  match mode:
      case "solo":
        dice_rolled = dice_roll(num_dice)
        print(f"you rolled {dice_rolled}")
        if 7 in dice_rolled:
          winnertext = pyfiglet.figlet_format(f"\n 7 7 7 7 7 \n you won with a 7 \n 7 7 7 7 7")
          print(winnertext)
        if any(x in dice_rolled for x in [2, 4, 8]):
          losertext = pyfiglet.figlet_format(f"you lost you rolled {dice_rolled}")
          print(losertext)
          return keep_playing(False, dice, mode)
        else:        
          reroll = input(f"\n close you rolled {dice_rolled} Wanna roll again").lower().strip()
          if reroll in positives:
            keep_playing(True, dice, mode)

          elif reroll in negatives or reroll in close_out:
            keep_playing(False, dice, mode)
          else:
            print("invalid")
            games()  

      case "vs":
        print("\n vs mode not done yet")
        backhome()

      case _:  
        badpull = input(f"you input gid something wrong \n 1) back to games list \n 2) back to menu \n 3) back to dice {mode} mode ") 
        if badpull == "1":
          games()
        if badpull == "2":
          menu()
        if badpull == "3":
          dice(mode)

def choice():
    while True:
        pick = input(f"\n hello today is {today:%B %d, %Y}\n 1) Add new event \n 2) View events \n 3) Close program \n 4)delete a event \n   ")
        match pick:
            case "1":
                while True:
                    event = input("\n What you got todo? ")
                    timeofevent = input(f"what time is {event} 1-12? ").strip()
                    if timeofevent.isdigit():
                        timeofevent = int(timeofevent)
                        break
                    else:
                        print("\n invalid input")

                if 1 <= timeofevent <= 12:
                    while True:
                        amorpm = input(f"\n is {timeofevent} AM/PM ").strip().upper()
                        if amorpm in ["AM", "PM"]:
                            event_time = f"{timeofevent:02}:00 {amorpm}"
                            confirm = input(f"\n Confirm event '{event}' at {event_time}? (Y/N) ").strip().upper()
                            if confirm == "Y":
                                todos[event] = event_time
                                print("\n CONFIRMED")
                                break
                            elif confirm == "N":
                                print("\n event cancelled")
                        else:
                            print("\n Y or N only")


            case "2":
                for i, event in enumerate(todos, start=1):
                    print(f"{i}. {event}. @ {todos[event]}")
                print(f"\n you have {len(todos)} events in your todo list")


            case "3":
                yayornay = input("\n we done Y or N").upper().strip()
                if yayornay == "Y":
                    downkill = input("\n u sure").lower().strip()
                    if downkill in positives:
                        print("\n bye")
                        break
                else:
                    print("\n we go on")

            case "4":
                del_event = input("\n what event would you like to delete? ")
                if del_event in todos:
                  com_del = input(f"\n you sure \n Your about to delete {del_event} \n you will have to remake it if deleted   ")
                  if com_del in positives:
                    print(f"\n {del_event} deleted")
                    del todos[del_event]
                    return menu()
                  
                  elif com_del in negatives:
                    print("\n canceled")
                    menu()
                  
                  else:
                    print("\n canceled")
                    menu()


            case _:
                print("\n invalid choice")

gamesandmodes = {
    "1": {"name": "tic tac toe", "function": tic_tac_toe, "modes": ["solo", "vs"]},
    "2": {"name": "mine sweeper", "function": mine_sweeper, "modes": ["solo", "vs"]},
    "3": {"name": "chess", "function": chess, "modes": ["solo", "vs"]},
    "4": {"name": "dice", "function": dice, "modes": ["solo", "vs"]},
}


menu()
