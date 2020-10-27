def loop():
    a = 10
    #while loop with else block getting invoked
    while a > 0:
        print(a)
        a =a- 1
    else:
        print("Loop is finished")
    
    #while loop without else block getting invoked
    # In below while loop checks true(1 or any positive value) or false(0) it goes to infinite bcoz flag is always true in order to stop press Ctrl+c
    flag=1
    while flag:
        print("Flag is enabled so it becomes true")