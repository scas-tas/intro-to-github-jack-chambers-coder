import random
import time
List_of_selected_animals = []
division_1of2 = []
division_2of2 = []
division_number = 1
divisions = {
   1: division_1of2,
   2: division_2of2
}
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
   division_1of2 = []
   division_2of2 = []

def get_random_buff(): # Gets a random number for the buff
    return random.randint(1, 12)

def get_random_number(): # Gets a random number for the amount of animals fighting
    return random.randint(1,4)

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
      return(f"Round {round_number}: {animal_1} vs {animal_2}: {animal_1} wins!")
   elif power_2 > power_1:
      divisions[get_div_number()].append(animal_2)
      return(f"Round {round_number}: {animal_1} vs {animal_2}: {animal_2} wins!")
   else:
      divisions[get_div_number()].append(animal_1)
      divisions[get_div_number()].append(animal_2)
      return(f"Round {round_number}: {animal_1} vs {animal_2}: Draw!")

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

while True: # The animal selection process
   animal_search = input("Search up an animal: ")
   if animal_search == "":
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
           break
        else:
           print("Enter y/n! ")
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

while len(divisions[division_number]) != 1 :
   while True:
      determine_iterable(match_ups)

      if num1 >= len(match_ups) or num2 >= len(match_ups):
         if len(match_ups) % 2 != 0:
            bye_index = match_ups[-1]
            bye_animal = divisions[division_number][bye_index]
            print(f"{bye_animal} got a bye!")
            divisions[get_div_number()].append(bye_animal)
         break
      print(get_winner(divisions[division_number][match_ups[num1]], divisions[division_number][match_ups[num2]]))
      round_number += 1
   divisions[division_number] = []

   reset()
   if division_number == 1:
      division_number = 2
   else:
      division_number = 1
   get_matchup(divisions[division_number])
   move_on = input("Click enter to move on to the next phase! ")


print("-"*70)
print("The tournament is over!")
print("-"*70)
print("Calculating the winner", end="", flush=True)

for i in range(3):
    time.sleep(1)
    print(".", end="", flush=True)
print()
print(f"{divisions[division_number][0]} claims victory!!!")



