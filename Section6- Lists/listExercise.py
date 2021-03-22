#def eggs(someParameter):
#    someParameter.append('Hello')

#spam = [1, 2, 3] #mutable data type
#eggs(spam)
#print(spam)


import copy

spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
cheese[1] = 42
print('cheese', cheese)
print('spam', spam)
