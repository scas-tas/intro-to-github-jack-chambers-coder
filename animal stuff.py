import random

def get_random_buff():
    return random.randint(1, 12)

def get_random_number():
    return random.randint(1,4)

def get_winner(animal_1, animal_2):
   if dictionary1[animal_1()]




dictionary1 = {'Attercop': {
  'Type': "Spider",
  "Base_Strength": 2,
  "amount" : get_random_number()
  },
    "Newt:" : {
    "Type:": "Lizard",
    "Base_Strength": 4,
    "amount": get_random_number()
    },
      "Pismire" : {
      "Type": "Ant",
      "Base_Strength": 1,
      "amount": get_random_number()
      },
        "Steed":{
        "Type": "Horse",
        "Base_Strength": 7,
        "amount": get_random_number()
        },
          "Erne":{
          "Type": "Eagle",
          "Base_Strength": 7,
          "amount": get_random_number()
          },
            "Nightbird":{
            "Type": "Owl",
            "Base_Strength": 3,
            "amount": get_random_number()
            },
              "Warg":{
              "Type": "Wolf",
              "Base_Strength": 11,
              "amount": get_random_number()
              },
                "Reynard":{
                "Type": "Fox",
                "Base_Strength": 10,
                "amount": get_random_number()
                },
                  "Cony":{
                  "Type": "Rabbit",
                  "Base_Strength": 4,
                  "amount": get_random_number()
                  },
                    "Shark":{
                    "Type": "Seadog",
                    "Base_Strength": 9,
                    "amount": get_random_number()
                    },
                      "Paddok":{
                      "Type": "Frog",
                      "Base_Strength": 4,
                      "amount": get_random_number()
                      },
}

word = input("Enter a word: ")
if word.lower() in dictionary1:
  print(dictionary1[word.lower()])
else:
  print("Not in the dictionary!")
