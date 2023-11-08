import time



def mod_1():

def mod_2():

def mod_3():

def mod_4():

def mod_5():

def mod_6():

def mod_7():

def mod_8():

def sys_input():
  sys_list = ["mod_1", "mod_2", "mod_3", "mod_4", "mod_5", "mod_6", "mod_7", "mod_8" ]
  if "mod_1"

def life_status(curlifestatus):
  if curlifestatus == True:
    pass
  elif curlifestatus == False:
    print("\nyou died, try again, or rage quit...")
    exit()

print("You awake in a crypt, its dome ceiling reaching out into the darkness, as you awake...")

print("\nWhat do you do?\n")

get_input = input()

timer = 0
timey = True

while timey:
  try:
    if get_input == "Go outside and look around":
      print("You smell nothing but rotting wood of the colossal trees and morning dew on the underbrush bellow as you walk to what appears to be a Escarpment of this dammed wood, and from the small glimpse you get through the gloomy film of fog you see a ruined keep and the levatus shadowy shape apon its walls")
      if get_input != '':
        timey = False
        sys_input()
      input()
    elif get_input == "Go back to sleep":
      print("You drift into a sound sleep, slowly engulfued by the lingering fog, driven into a a peaceful indefinite slumber")
      if get_input != '':
        timey = False
      life_status(False)
  except:
    for i in range(15):
      timer = timer + i
      print(timer)
      if timer > 15:
        pass
      elif timer <= 15:
        life_status(False)
      else:
        quit()