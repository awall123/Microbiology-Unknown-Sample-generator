#Author: Andrew Wall, 10/26/2021
import random

grampos = ["B. subtilis", "B. cereus", "C. pseudodiptheriticum", "C. xerosis", "E. faecalis", "L. lactis", "M. luteus", "M. roseus", "M. smegmatis", "S. agalactiae", "S. aureus", "S. epidermidis", "S. pyogenes"]
gramneg = ["E. aerogenes", "E. coli", "K. pneumoniae", "P. aeruginosa", "P. fluorescens", "P. mirabilis", "P. vulgaris", "S. flexneri", "S. marcescens", "S. typhimurium"]

print("Current list of Unknown cultures used:\n")
print("Gram Positive:")
print(*grampos, sep = ", ")
print("")
print("Gram Negative:")
print(*gramneg, sep = ", ")
print("")

def addpos():
    fpos = input("Type a single name and press 'Enter'.\n Example: E. coli\n")
    grampos.append(fpos)

a = input("Would you like to add any Gram positive bacteria to the current list?\nType: Y or N\n")

def checkpoint_pos():
    if (a == 'Y'):
        z =int(input("How many species of bacteria would you like to add?\n"))
        for _ in range(z):
            addpos()
    elif (a == 'y'):
        z =int(input("How many species of bacteria would you like to add?\n"))
        for _ in range(z):
            addpos()

checkpoint_pos()

print("")
print("Current Gram positive list:")
print(*grampos, sep = ", ")

print("")

def addneg():
    fneg = input("Type a single name and press 'Enter'.\n Example: E. coli\n")
    gramneg.append(fneg)

b = input("Would you like to add any Gram negative bacteria to the current list?\nType: Y or N\n")

def checkpoint_neg():
    if (b == 'Y'):
        x =int(input("How many species of bacteria would you like to add?\n"))
        for _ in range(x):
            addneg()
    if (b == 'y'):
        x =int(input("How many species of bacteria would you like to add?\n"))
        for _ in range(x):
            addneg()

checkpoint_neg()

print("")
print("Current Gram negative list:")
print(*gramneg, sep = ", ")

print("")

def unknown():
	x = random.randint(1,20)
	y = (x/20)
	if (y == 0.05):
		item1 = random.choice(grampos)
		item2 = random.choice(grampos)
		print (item1, item2, sep = "\t")
	elif (y == 0.1):
		item1 = random.choice(gramneg)
		item2 = random.choice(gramneg)
		print (item1, item2, sep = "\t")
	else:
	    item1 = random.choice(grampos)
	    item2 = random.choice(gramneg)
	    print (item1, item2, sep = "\t")

students = int(input("Enter the number of students needing Unknown pairs and press 'Enter'\n "))
print ("")
for _ in range(students):
    unknown()

print("")
input("Highlight the above list and copy to excel.\nPress 'Enter' when finished")
