l = [['40', '20', ], ['20', '30', '20'], ['30', '20'], ['100', '100'], ['100'], ['100']]

newList=[]
newList = [[float(y) for y in x] for x in l]

print(newList)