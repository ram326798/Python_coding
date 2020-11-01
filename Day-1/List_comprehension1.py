def List_comprehension1():
    a=[1,3,3,4,5,6]
    b=[i**2 for i in a if i%2 !=0]
    print(b)