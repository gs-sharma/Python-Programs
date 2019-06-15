import json                                                           #to load json data we use this library
from difflib import get_close_matches                                 #to find simillarity metric in 2  - difflib
data = json.load (open("data.json"))                                  #type = Dictionary

def translate(w):                                                     #function to return the meaning of word
    if w in data:                                                     #to check if word is present in data
        return data[w]
    elif len(get_close_matches(w , data.keys())) > 0:                 #find a match , if no match found = 0
        yn = input( "Did you mean %s instead ? Enter Y if Yes , or N for No : " %get_close_matches(w ,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w ,data.keys())[0]]         #return the first match found
        elif yn == "N":
            return "Sorry !! Better Luck Next Time :"
        else :
            return "Wrong Choice"

    else:
        print( "The word doesent exist , Please Check again !!")
        opt = input("Want to Search again :")
        options(opt)
        return  "Happy to Help"

def take_input():
    word = input("input word : ");
    word = word.lower()                                              #To conver input to lower-case
    output = translate(word)
    if type(output) == list :
        for i in output:
            print(i)
    else:
        print(output)
    return "Happy To Help"

def options(opt):                                                    #to provide the user a choice to search again
    opt = opt.lower()
    if (opt == "y"):
        take_input()
    else:
        return "Sorry ! Better Luck next Time"

take_input()
