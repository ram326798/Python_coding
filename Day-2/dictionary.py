l=[1,2,3]

#sqares of dictionary
y={i:i*i for i in l}
print(y)

#using list comprehension

x=[i for i in y.items()]
print(x)
list(y.values())

x=[i*i for i in l]
print(x)
