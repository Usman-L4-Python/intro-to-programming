active = True
while active:
    topp = input("Enter a topping: ")
    
    if topp == 'quit':
        active = False
    else:
        print("Adding "+topp+" to the pizza toppings.")
        print('Enter quit to exit ol')
#Write 'quit' to Exit .