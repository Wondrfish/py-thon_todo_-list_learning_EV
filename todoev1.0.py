import datetime
from time import sleep
from tqdm import tqdm

today = datetime.date.today()

positives = ["yeah", "yes", "shut down", "y"]
negatives = ["no", "nope", "nah", "n", "no way jose"]
close_out = ("close", "exit", "quit")

def backhome():
  print("back to menu")
  menu()

def menu():
  print(f"Today is {today}")
  task = input("\nWhat Are we doing today \n\n 1)Task manager \n 2)calculator \n 3) file cleaner \n 4) games \n")
  if task == "1":
    choice()
  if task == "2":
    print("calc not done yet")
    #calculator()
  if task == "3":
    print("file cleaner not done yet")
    #file_cleaner()
  if task == "4":
    games()

def games():
  pick_a_game = input("\nwhat do you wanna play \n 1)tic tac toe \n 2) mine sweeper \n 3) chess    \n").lower()
  gamepicked = {
      "tic tac toe": ["solo", "vs"],
      "mine sweeper": ["solo", "vs"],
      "chess": ["solo", "vs"]
}
  if pick_a_game in gamepicked:
      mode = input(f"\n You picked {pick_a_game}\n are you playing solo or vs mode").lower()
      if mode in gamepicked[pick_a_game]:
        print(f" opening {pick_a_game} in {mode} mode")
        for i in tqdm(range(10)):#sim loading
          sleep(2)
        print(f"\n {pick_a_game} is ready enjoy")
  if pick_a_game in close_out:
    backhome()
  else:
    print(f"\n {pick_a_game} was not a choice")
    games()



def choice():
    todos = {}
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
                input("\n what  event would you like to delete? ")
                if event in todos:
                  com_del = input(f"\n you sure \n Your about to delete {event} \n you will have to remake it if deleted   ")
                  if com_del in positives:
                    print(f"\n {event} deleted")
                    del todos[event]
                  else:
                    print("\n canceled")


            case _:
                print("\n invalid choice")


menu()
