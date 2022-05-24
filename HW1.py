
"""
Program to input all the data from the files to dictionary sorted and only with alphabet and lowercase words.
"""


all_files = ["names.txt","colors.txt","cities.txt","fruit.txt"]
Dict = {}
for file in all_files:
  with open(file) as f:
     for line in f:
        for word in line.split():
         if word.isalpha():
            word = word.lower()
            if word in Dict and file == "names.txt":
               Dict[word].add("names")
            elif word in Dict and file == "colors.txt":
               Dict[word].add("colors")
            elif word in Dict and file == "cities.txt":
               Dict[word].add("cities")
            elif word in Dict and file == "fruit.txt":
               Dict[word].add("fruit")
            else:
                Dict[word] = {file[:-4]}


with open("dictionary.txt","w") as f:
    f.write(repr(Dict))
    

