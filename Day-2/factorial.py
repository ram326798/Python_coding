class Factorial:
    
  def __init__(self, num):
    self.num = num

  def myfunc(self):
      a=1
      while self.num!=0 :
          a= a*self.num
          self.num=self.num-1
      print(a)
#   def _repr_(self):
#       a=1
#       while self.num!=0 :
#           a= a*self.num
#           self.num=self.num-1
#       print(a)
# below str function is used for string not for int,long,float,double
      
#   def _str_(self):
#       a=1
#       while self.num!=0 :
#           a= a*self.num
#           self.num=self.num-1
#       print("in str function"+a)
   
      
p1 = Factorial(int(input("Enter number : ")))
p1.myfunc()
# p1._str_()
# p1.__repr_()
