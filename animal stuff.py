import random
import time
List_of_selected_animals = []
semi_finals = []
def reset():
   global match_ups, num1, num2, round_number
   match_ups = []
   num1 = -2
   num2 = -1
   round_number = 1
   
def get_random_buff():
    return random.randint(1, 12)

def get_random_number():
    return random.randint(1,4)

def get_matchup(list):
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
      e = "z"
   else:
    num1 += 2
    num2 += 2

def get_winner(animal_1, animal_2):
   power_1 =  dictionary1[animal_1]["Base_Strength"] + dictionary1[animal_1]["Base_Strength"] * 0.5 * (dictionary1[animal_1]["amount"])
   power_2  = dictionary1[animal_2]["Base_Strength"] + dictionary1[animal_2]["Base_Strength"] * 0.5 * (dictionary1[animal_2]["amount"])
   if power_1 > power_2:
      semi_finals.append(animal_1)
      return(f"Round {round_number}: {animal_1} vs {animal_2}: {animal_1} wins!")
   elif power_2 > power_1:
      semi_finals.append(animal_2)
      return(f"Round {round_number}: {animal_1} vs {animal_2}: {animal_2} wins!")
   else:
      semi_finals.append(animal_1)
      semi_finals.append(animal_2)
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

while True:
   animal_search = input("Search up an animal: ")
   if animal_search == "":
      break_it = input("Click enter again to continue to the tournament!")
      if break_it == "":
         break
   if animal_search.title() in dictionary1:
      print(f"Type: {dictionary1[animal_search.title()]["Type"]}")
      print(f"Base Strength: {dictionary1[animal_search.title()]["Base_Strength"]}")
      if animal_search in List_of_selected_animals:
          print("-"*70)
          print("This animal is already in the tournament!")
          print("-"*70)
          continue
      while True:
        yes_or_no = input("Would you like to add this animal to the tournament? y/n: ")

        if yes_or_no.lower() in ["y", "yes"]:
          List_of_selected_animals.append(animal_search.title())
          print("-"*70)
          print("Animal added to the tournament!")
          print("-"*70)
          print("Current tournament players:")
          for animal in List_of_selected_animals:
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
print("Which animal do you think will win?")
for animal in List_of_selected_animals:
   print(f"{animal} ({chr(ord("A") + letter_count)})")
   animal_letter[animal.title()] = chr(ord("A") + letter_count)
   letter_count += 1
while True:
  selected_animal = input(f"Select an animal you think will win using the corresponding letter: ")
  if selected_animal.upper() in animal_letter.values():
     break
  print("Invalid")

get_matchup(List_of_selected_animals)


while True:
   determine_iterable(match_ups)
   if num1 >= len(match_ups) or num2 >= len(match_ups):
      if len(match_ups) % 2 != 0:
         bye_index = match_ups[-1]
         bye_animal = List_of_selected_animals[bye_index]
         print(f"{bye_animal} got a bye!")
         semi_finals.append(bye_animal)
         break
   print(get_winner(List_of_selected_animals[match_ups[num1]], List_of_selected_animals[match_ups[num2]]))
   round_number += 1
match_ups = []
num_1 = -2
num_1 = -1
get_matchup(semi_finals)

""""
while True:
   determine_iterable(semi_finals)
   if num1 >= len(semi_finals) or num2 >= len(semi_finals):
      if max(match_ups) % 2 == 0:
         print(f"{List_of_selected_animals[match_ups[match_ups.index(max(match_ups))]]} got a bye!")
         semi_finals.append(List_of_selected_animals[match_ups[match_ups.index(max(match_ups))]])
         print(semi_finals)
         break
   print(get_winner(List_of_selected_animals[match_ups[num1]], List_of_selected_animals[match_ups[num2]]))
   print(semi_finals)
   round_number += 12
"""