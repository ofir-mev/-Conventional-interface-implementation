
"""
Program to clean the text and input in the list only the alphabet and lowercase words and sorted them.
"""


Dict = {}
with open("dictionary.txt") as f:
   Dict= eval(f.read())



list = []
c=0
with open("text.txt") as f:
     for line in f:
        for word in line.split():
            if word[0]=="," or word[0]=="?" or word[0]=="!" or word[0]==".":
                word = word[1:]
                word=word.lower()
            elif word[-1]=="," or word[-1]=="?" or word[-1]=="!" or word[-1]==".": 
                word = word[:-1]
                word=word.lower()
            if word.isalpha():
                word=word.lower()
                if word in Dict:
                   tuple=(word,c+1,Dict[word])
                   temp =(Dict[word])
                else:
                    tuple=(word,c+1,{})
                    temp =({})
                for tup in list:
                   if tuple[0] in tup:
                      x = tup[1]
                      index = list.index(tup)
                      list.remove(tup)
                      tuple=(word,x+1,temp)
                      list.insert(index, tuple)
                      break
                if tuple not in list:
                    list.append(tuple)


with open("words.txt","w") as f:
    f.write(repr(sorted(list,key=lambda x:(-x[1],x[0]))))
