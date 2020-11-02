def myFun(*args,**kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
    
    
#   >>myFun('ram','python','vue',firstname="Ram",lastname="Krish",coding="python")
#output:
#args:  ('ram', 'python', 'vue')
#kwargs:  {'firstname': 'Ram', 'lastname': 'Krish', 'coding': 'python'}
