def odd_numbers_square():
    a=[1,3,3,4,5,6]
    for i in range(0,6):
        if (a[i]%2 !=0):
            a[i]=a[i]**2
    print(a)