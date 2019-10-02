
def myHash0(value):
    return len(value)  # constant time


bobAddress = myHash0('bob')  # --> 3
ahmedAddress = myHash0('ahmed')  # --> 5

myArray = [None] * 8

myArray[bobAddress] = 'bob'
myArray[ahmedAddress] = 'ahmed'

print(myArray[bobAddress])

print(myArray[myHash0('bob')])
