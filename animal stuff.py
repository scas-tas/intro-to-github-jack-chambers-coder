import random
import time
List_of_selected_animals = []
division_1of2 = []
division_2of2 = []
phase = 1
division_number = 1
divisions = {
   1: division_1of2,
   2: division_2of2
}
def sleep():
   time.sleep(1)
   return ""
def calculating_winner_delay(): # Creates a delay for a calculation effect
   if len(match_ups) != 2:
      print(f"Beginning round {round_number} ", end="", flush=True)
      for i in range(3):
         time.sleep(1)
         print(".", end="", flush=True)
      time.sleep(1)
      print()
   else:
      return

def next_phase_delay(): # Creates a delay between phases
   print("-"*70)
   print()
   print(f"MOVING ON TO PHASE {phase} ", end="", flush=True)
   for i in range(3):
      time.sleep(1)
      print(".", end="", flush=True)
   time.sleep(1)
   print()
   print()
   print("-"*70)

def get_div_number():
   if division_number == 1:
      return 2
   else:
      return 1

def reset(): # resets the values
   global match_ups, num1, num2, round_number, division_1of2, division_2of2
   match_ups = []
   num1 = -2
   num2 = -1
   round_number = 1

def get_random_number(): # Gets a random number for the amount of animals fighting
    return random.randint(1,10)

def get_matchup(list): # Creates a new list of integers (match_ups) matching the amount of values in list
   while len(match_ups) != len(list):
    randomed = random.randint(0, len(list)-1)
    if randomed in match_ups:
       continue
    else:
      match_ups.append(randomed)
   return(match_ups)

def determine_iterable(list):
   global num1, num2
   if num1 >= len(list) or num2 >= len(list):
      return
   else:
    num1 += 2
    num2 += 2

def get_winner(animal_1, animal_2): # Gets the winner based on two animals fighting
   power_1 =  dictionary1[animal_1]["Base_Strength"] + dictionary1[animal_1]["Base_Strength"] * 0.5 * (dictionary1[animal_1]["amount"])
   power_2  = dictionary1[animal_2]["Base_Strength"] + dictionary1[animal_2]["Base_Strength"] * 0.5 * (dictionary1[animal_2]["amount"])
   if power_1 > power_2:
      divisions[get_div_number()].append(animal_1)
      print(f"Round {round_number}: {animal_1} vs {animal_2}:")
      time.sleep(1)
      print(f"{animal_1} has spawned in a group of {dictionary1[animal_1]['amount']}!")
      time.sleep(1)
      print(f"{animal_2} has spawned in a group of {dictionary1[animal_2]['amount']}")
      time.sleep(1)
      if len(match_ups) != 2:
         print("Calculating winner...")
         time.sleep(1)
         print(f"{animal_1} wins!")
   elif power_2 > power_1:
      divisions[get_div_number()].append(animal_2)
      print(f"Round {round_number}: {animal_1} vs {animal_2}:")
      time.sleep(1)
      print(f"{animal_1} has spawned in a group of {dictionary1[animal_1]['amount']}!")
      time.sleep(1)
      print(f"{animal_2} has spawned in a group of {dictionary1[animal_2]['amount']}!")
      time.sleep(1)
      if len(match_ups) != 2:
         print("Calculating winner...")
         time.sleep(1)
         print(f"{animal_2} wins!")
   else:
      divisions[get_div_number()].append(animal_1)
      divisions[get_div_number()].append(animal_2)
      print(f"Round {round_number}: {animal_1} vs {animal_2}:")
      time.sleep(1)
      print(f"{animal_1} has spawned in a group of {dictionary1[animal_1]['amount']}!")
      time.sleep(1)
      print(f"{animal_2} has spawned in a group of {dictionary1[animal_2]['amount']}!")
      time.sleep(1)
      print("Calculating winner...")
      time.sleep(1)
      print("Draw!")

letter_count = 0
yes_or_no = "?"
animal_letter = {}

dictionary1 = {'Spider': {
  'Type': "Attercop",
  "Base_Strength": 2,
  "amount" : get_random_number()
  },
    "Lizard" : {
    "Type": "Newt",
    "Base_Strength": 4,
    "amount": get_random_number()
    },
      "Ant" : {
      "Type": "Pismire",
      "Base_Strength": 1,
      "amount": get_random_number()
      },
        "Horse":{
        "Type": "Steed",
        "Base_Strength": 7,
        "amount": get_random_number()
        },
          "Eagle":{
          "Type": "Erne",
          "Base_Strength": 7,
          "amount": get_random_number()
          },
            "Owl":{
            "Type": "Nightbird",
            "Base_Strength": 3,
            "amount": get_random_number()
            },
              "Wolf":{
              "Type": "Warg",
              "Base_Strength": 11,
              "amount": get_random_number()
              },
                "Fox":{
                "Type": "Reynard",
                "Base_Strength": 10,
                "amount": get_random_number()
                },
                  "Rabbit":{
                  "Type": "Cony",
                  "Base_Strength": 4,
                  "amount": get_random_number()
                  },
                    "Shark":{
                    "Type": "Seadog",
                    "Base_Strength": 9,
                    "amount": get_random_number()
                    },
                      "Frog":{
                      "Type": "Paddok",
                      "Base_Strength": 4,
                      "amount": get_random_number()
                      },
}

print("-"*120)
for letter in "Welcome guest to the archaic library, search up one of the following animals to uncover their archaic terms!":
   print(letter, end="", flush=True)
   time.sleep(0.04)
time.sleep(2)

print(f"\n| Collecting animal data", end="", flush=True)
for i in range(3):
   time.sleep(1)
   print(".", end="", flush=True)
time.sleep(1)
print()
for animal in dictionary1:
   print(animal) 
   time.sleep(0.3)
print("-"*120)


while True: # The animal selection process
   animal_search = input("Search up an animal (c to continue): ")
   if animal_search == "c":
      if len(divisions[division_number]) <= 1:
         print("You do not have enough animals selected to continue!")
      else:
         break_it = input("Click enter again to continue to the tournament!")
         if break_it == "":
            break
   if animal_search.title() in dictionary1:
      print(f"Type: {dictionary1[animal_search.title()]["Type"]}")
      print(f"Base Strength: {dictionary1[animal_search.title()]["Base_Strength"]}")
      if animal_search.title() in divisions[division_number]:
          print("-"*70)
          print("This animal is already in the tournament!")
          print("-"*70)
          continue
      while True:
        yes_or_no = input("Would you like to add this animal to the tournament? y/n: ")

        if yes_or_no.lower() in ["y", "yes"]:
          divisions[division_number].append(animal_search.title())
          print("-"*70)
          print("Animal added to the tournament!")
          print("-"*70)
          print("Current tournament players:")
          for animal in divisions[division_number]:
             print(animal.title())
          print("-"*70)
          break

        elif yes_or_no.lower() in ["n", "no"]:
           print("-"*70)
           print("Animal not added to the tournament.")
           print("-"*70)
           break
        else:
           print("Enter y/n! ")
   else:
      if animal_search == "c":
         continue
      else:
         print("Not in the dictionary")


reset() 
print("Which animal do you think will win?")  #Chosen animal selection process
for animal in divisions[division_number]:
   print(f"{animal} ({chr(ord("A") + letter_count)})")
   animal_letter[animal.title()] = chr(ord("A") + letter_count)
   letter_count += 1
while True:
  selected_animal = input(f"Select an animal you think will win using the corresponding letter: ")
  if selected_animal.upper() in animal_letter.values():
     break
  print("Invalid")


get_matchup(divisions[division_number]) #Uses the function to randomise the battles
next_phase_delay()
while len(divisions[division_number]) != 1 :
   while True:
      determine_iterable(match_ups)

      if num1 >= len(match_ups) or num2 >= len(match_ups):
         if len(match_ups) % 2 != 0:
            bye_index = match_ups[-1]
            bye_animal = divisions[division_number][bye_index]
            time.sleep(1)
            print(f"{bye_animal} got a bye!")
            print("-"*70)
            divisions[get_div_number()].append(bye_animal)
         break
      calculating_winner_delay()
      print("-"*70)
      if len(match_ups) != 2:
         get_winner(divisions[division_number][match_ups[num1]], divisions[division_number][match_ups[num2]])
      else:

         print(f"The final battle is between {divisions[division_number][match_ups[num1]]} and {divisions[division_number][match_ups[num2]]}!")
         print("-"*70)
         time.sleep(0.3)
         get_winner(divisions[division_number][match_ups[num1]], divisions[division_number][match_ups[num2]])
      print("-"*70)
      round_number += 1
   for animal in divisions[division_number]:
      dictionary1[animal]["amount"] = get_random_number()

   divisions[division_number] = []
   division_number = get_div_number()
   if len(divisions[division_number]) == 1:
        break

   reset()

   get_matchup(divisions[division_number])
   print("Remaining contestants:")
   for animal in divisions[division_number]:
      print(animal)
   print("-"*70)
   phase += 1
   move_on = input("Click enter to move on to the next phase! ")
   next_phase_delay()


print("-"*70)
print("Calculating the winner", end="", flush=True)

for i in range(3):
    time.sleep(1)
    print(".", end="", flush=True)
print()
print("-"*70)
print(f"{divisions[division_number][0]} claims victory!!!")
print("-"*70)

if animal_letter[divisions[division_number][0]] == selected_animal.upper():
   print("Your chosen animal won!")
else:
   print("You chose incorrectly...")
print("-"*70)

