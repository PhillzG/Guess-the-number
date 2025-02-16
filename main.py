import random
number = random.randint(1, 100)



while True:
    user_input = input("Daj numer miedzy 1 a 1000(exit to quit) ")
    if user_input == "exit" or "quit":
        print ("thanks for playing! ")
        break
    try: 
        guess=int(user_input)
        
        if guess <1 or guess >1000:
            print ("zla liczba")
            continue

        if guess > number:
            print ("Za duzo")
        elif guess < number:
            print ("Za malo")
        else: 
            print ("Poggers, zgadles")
            break


    except ValueError:
        print("Liczba mordo :3")    