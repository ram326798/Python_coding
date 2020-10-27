def multiples():
    import random
    a = int(input("Emter Lower bound:- "))

    b = int(input("Enter Upper bound:- "))

    c = random.randint(a, b)
  #In order to know the randow value   print(c)

    guess = int(input("Guess a number:- "))

    
    if c>guess:
        print("your guess  is lower")
    elif c<guess:
        print("Your guess is higher")
    elif c==guess:
        print("your guess  is perfect")
    