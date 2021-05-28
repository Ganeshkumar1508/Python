import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0 :
        print("did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("press y for yes or n for no \n").lower()
        if decide == "y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n":
            return("You have entered wrong word, Please check again... ")
        else:
            return("You have entered wrong word please enter only y or n \n")
    else:
        print("You have entered wrong word, Please check again...")


q = "y"
while (q=="y"):
    word = input("Enter the word you want to search: ")
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)

    q=input("Do you want to search again? if yes press y or press anyother key: ").lower()

    