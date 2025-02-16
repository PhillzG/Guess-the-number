import random
number = random.randint(1, 1000)

def hint(guess, number):
    difference = abs(guess-number)
    if difference >=100:
        print()
        return " W chuj roznicy stary"
    elif difference >=10:
        print()
        return " Juz lepiej"
    else:
        print()
        return " Blisko" 


while True:
    user_input = input("Daj numer miedzy 1 a 1000(exit zeby wyjsc) ").lower()
    if user_input == "exit":
        print ("Adios! ")
        break
    try: 
        guess=int(user_input)
        
        if guess <1 or guess >1000:
            print ("zla liczba")
            continue

        if guess > number:
            print ("Za duzo "+hint(guess,number))
            print()
        elif guess < number:
            print ("Za malo "+hint(guess,number))
            print()
        else: 
            print ("Poggers, zgadles")
            print()
            break


    except ValueError:
        print("Liczba mordo :3")    