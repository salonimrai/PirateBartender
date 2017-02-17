import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}


def askPreferences():
    answers = {}
    for key, value in questions.items():
        ans = str(input(value + "  --->  "))
        if (ans.lower()=='y' or ans.lower()=='yes'):
            answers[key]=True
        else:
            print("You didn't say yes so we'll take that as a no")
            answers[key]=False
    print(answers)
    return answers

    
def makeDrink(preferences):
    drink = []
    for k, v in preferences.items():
        if(preferences[k]):
            ing = random.choice(ingredients[k])
            print("Adding {0} from {1}".format(ing, k))
            drink.append(ing)
        else:
            print("No ingredient from: {0}".format(k))
    print(drink)
    

if __name__=="__main__":
    makeDrink(askPreferences())

            
            