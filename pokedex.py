name_dict = {}
num_dict = {}
import urllib.request
import re
def create_Pokedex(link):
    """Creates Pokedex. Takes a link as an argument, creates two dictionaries."""
    global name_dict #changes the global dictionaries which are accessed in other functions
    global num_dict
    response = urllib.request.urlopen(link)
    html = response.read()
    matches = re.findall('<td>(\d+)</td>\\\\n<td><a href="/wiki/.*?>(.*?)</a>',str(html))
    for match in matches:
        (number, name) = match
        name_dict[name] = number
        num_dict[int(number)] = name
def print_by_number():
    """Takes no argument, prints in numerical order"""
    numlist = list(num_dict)
    for i in range(len(num_dict.keys())):
        print (numlist[i], num_dict[numlist[i]]) #gets the corresponding value in the dictionary for the number, since it's all in number order
alphabetical_list = []
def print_by_name():
    """Sorts list of names alphabetically with no argument, then prints"""
    alphabetical_list = sorted(name_dict)
    for i in alphabetical_list:
        print (i)
def lookup_by_name(name_Pokemon):
    """Looks up by name as a key in the dictionary of names. Also makes it case insensitive. Name is user inputted as argument. Returns number or error"""
    name_Pokemon = name_Pokemon.lower()
    name_Pokemon = name_Pokemon.capitalize()  #allows for any case, would make all lower case then first letter uppercase to match key in dictionary
    if name_Pokemon in name_dict.keys():
        return (name_dict[name_Pokemon])
    else:
        return ("Invalid input")
def lookup_by_number(num_Pokemon):
    """Looks up by number, makes sure that it is a number and a number in the Pokedex. Number is user inputted as argument. Returns name or error"""
    if num_Pokemon.isdigit():   #tests if it is a number
        num_Pokemon = int(num_Pokemon)
        if num_Pokemon in num_dict.keys(): #tests if number in Pokedex
            return (num_dict[num_Pokemon])
        else:
            return ("Number not in Pokedex")
    else:
        return ("Invalid input")
def lookup_by_letter(letter):
    """Looks up by letter, makes sure that it is a letter, and only one letter. Letter is user inputted as argument, returns list of Pokemon or error"""
    letterlist = []
    if len(letter) == 1 and letter.isalpha(): #tests if input is a letter and only one letter
        letter = letter.capitalize() #allows for case insensitivity, makes uppercase to match dictionary keys
        for i in name_dict.keys():
            if i[0] == letter:
                letterlist.append(i)
        letterlist.sort()
        return (letterlist)
    else:
        return ("Invalid input")
print ("Welcome to the Pokedex. You will be able to sort Pokemon by name or number, as well as lookup Pokemon by their number, name, and first letter.") #only prints once
create_Pokedex('https://en.wikipedia.org/wiki/List_of_Pokemon')
while True:
    print ("1) Print the list of pokemon sorted by national pokemon index")
    print ("2) Print the list of pokemon sorted alphabetically by name")
    print ("3) Lookup pokemon by name and print number")
    print ("4) Lookup pokemon by number and print name")
    print ("5) Lookup all pokemon that start with a letter")
    print ("q) Quit")
    y = input ("What would you like to do? ")
    if y == "q":
        print ("Goodbye.")
        break
    elif y.isdigit():
        y = int(y)
    else:
        print ("Invalid input. Please try again.")
        continue  #if it's not a number, goes back to the beginning
    if y == 1:
        print_by_number()
    elif y == 2:
        print_by_name()
    elif y == 3:
        number = lookup_by_name(input("Which Pokemon would you like to look up? "))
        print (number)
    elif y == 4:
        name = lookup_by_number(input("What Pokemon number would you like to look up? "))
        print (name)
    elif y == 5:
        letter = lookup_by_letter(input("What letter would you like to look up? "))
        print (letter)
    else:
        print ("Invalid input. Please try again.")
        continue #if it's not a number between 1-5, goes back to the beginning
        
