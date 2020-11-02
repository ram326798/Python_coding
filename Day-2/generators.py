def PowTwoGen(max=5):
    n = 1
    while n <= max:
        yield n
        n += 1



#output:
# >>a=PowTwoGen()
# >>next(a)
# 1
# >>next(a)
#  2
# >>next(a)
#  3
# >>next(a)
#  4
# >>next(a)
#  5
# >>next(a)
#  StopIteration
  
  
