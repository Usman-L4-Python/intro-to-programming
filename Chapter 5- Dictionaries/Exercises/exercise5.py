Ash = {
    'species':'dog',
    'owner':'Usman',
    'name':'Ash',
}
Hunter = {
    'name':'Hunter',
    'species':'cat',
    'owner':'Usman',
}

pets = [Hunter,Ash]
for pet in pets:
    print(pet['name'].title()+' is a '+pet['species']+', and it belongs to '+
        pet['owner'].title()+'.')