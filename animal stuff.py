import random
import time
match_ups = []
num1 = -1
num2 = 0
def get_random_buff():
    return random.randint(1, 12)

def get_random_number():
    return random.randint(1,4)

def get_matchup():
   while len(match_ups) != len(List_of_selected_animals):
    match_ups.append(random.randint(1, len(List_of_selected_animals)))
   return(match_ups)

def determine_iterable():
   if num1 or num2 >= len(match_ups):
      e = "z"
   else:
    num1 += 1
    num2 += 1

def get_winner(animal_1, animal_2):
   if dictionary1(animal_1("Base_strength")) + dictionary1(animal_1("Base_strength")) * 1/2(dictionary1(animal_1("amount"))) > dictionary1(animal_2("Base_strength")) + dictionary1(animal_1("Base_strength")) * 1/2(dictionary1(animal_2("amount"))):
      print("soirgnsrgnionwsrg")

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
List_of_selected_animals = []

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
          List_of_selected_animals.append(animal_search)
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



print("Which animal do you think will win?")
for animal in List_of_selected_animals:
   print(f"{animal} ({chr(ord("A") + letter_count)})")
   animal_letter[animal] = chr(ord("A") + letter_count)
   letter_count += 1
while True:
  selected_animal = input(f"Select an animal you think will win using the corresponding letter: ")
  if selected_animal.upper() in animal_letter.values():
     break
  print("Invalid")

get_matchup()
while True:
   determine_iterable()
   print(get_winner(List_of_selected_animals(match_ups(num1)), List_of_selected_animals(match_ups(num2))))
