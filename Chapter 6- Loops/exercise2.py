while True:
    age = input("Enter your age: ")

    if age == 'quit':
        break
    
    age = int(age)
    if age < 3:
        print("Your ticket is free kid!")
    elif age <= 12:
        print("Your ticket is 100$")
    else:
        print("Your ticket is 150$")