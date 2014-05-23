import string
import math
import sys
import re
import random

list_of_books = []


declaration = open("C:/PATH/declaration.txt","r")
declaration = str(declaration.read())
declaration = "Declaration " + declaration.lower()
list_of_books.append(declaration)

constitution = open("C:/PATH/constitution.txt","r")
constitution = str(constitution.read())
constitution = "Constitution " + constitution.lower()
list_of_books.append(constitution)

print "Bookworm says: Challenge me with a quote :)"
while True:
    s = raw_input("""Your challenge: """)
    s = s.lower()
    if len(s)>10:
        for book in list_of_books:
            if s in book:
                name = book.split()[0]
                answer = random.choice(["Well, it must be the '","I suppose it is the'","I am sure as a computer program can be it is the'"]) + name + "'!"
                break    
        try:
            print "Bookworm: ", answer
        except NameError:
            print "I haven't found it anywhere"       
        
    else:

        print random.choice(["Give me a longer extract","Your phrase is too short","Type a longer phrase"])
        
import platform
if platform.system()=='Windows':
    input()
