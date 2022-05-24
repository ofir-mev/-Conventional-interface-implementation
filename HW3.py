

"""
The program will print every word that passed the Conditions while specifying why it went through the Conditions
"""
list =[]
with open("words.txt") as f:
     list = eval(f.read())
     for tup in list:
         if tup[1] >= 5 and len(tup[2]) > 1:
             print("'"+tup[0]+"'", "because it belongs to at least two categories and because it appears at least five times")
         elif tup[1] >= 5:
             print("'"+tup[0]+"'", "because it appears at least five times")
         elif len(tup[2]) > 1:
             print("'"+tup[0]+"'", "because it belongs to at least two categories")





