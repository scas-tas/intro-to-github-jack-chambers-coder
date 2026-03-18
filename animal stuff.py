import random

dictionary = {'attercop': {
  'Type': "A spider",
  "Base_Strength":
  "Buffed_Strength" : get_random_buff() + dictionary["attercop"["A spider"]]
  "amount" : get_random_number()


  'batrachophagous': 'To feed on frogs.',
    'chirotonsor': 'A barber.',
      'deltiologist': 'A postcard collector.',
        'erinaceous': 'Of hedgehogs.',
          'favillous': 'Looking like ashes.',
            'grimalkin': 'A cat.',
              'nelipot': 'Someone who goes barefoot often.',
                'pogonotomy': 'Cutting a beard.',
                  'psithurism': 'The sound of wind in the trees.',
                    'scolecophagous': 'To eat worms.',
                      'xerophagy': 'Eating only dry food.'}

word = input("Enter a word: ")
if word.lower() in dictionary:
  print(dictionary[word.lower()])
else:
  print("Not in the dictionary!")

def get_random_buff():
    return random.randit(1, 7)

def get_random_number()
    return random.randit(1,4)
