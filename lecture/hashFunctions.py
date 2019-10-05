
def myHash0(value):
    return len(value)  # constant time


bobAddress = myHash0('bob')  # --> 3
ahmedAddress = myHash0('ahmed')  # --> 5
dadAddress = myHash0('dad')

maryPoppins = myHash0('maryPoppins')

print(bobAddress)

myArray = [None] * 8

myArray[bobAddress] = 'bob'
myArray[dadAddress] = 'dad'
myArray[ahmedAddress] = 'ahmed'

print(myArray[bobAddress])

print(myArray[myHash0('bob')])


# What is its speed?  Fast
# Not unique at all! NAME COLLISION
# Non-invertible

# Here is the hash table: {hashFunction: (), self.storage: [(key, value)]}


def myHash1(key):
    stringIndex = 0
    for char in key:
        if char == 'a':
            stringIndex += 1

        if char == 'b':
            stringIndex += 2

            # ... and so on

    return stringIndex

# dad -> 9
# bob -> 2 + 2 + 'o' --> different number
# FEWER name collisions
# Kind of invertible

# what could make a 9?  add, dad, I


def myHash2(key):
    stringIndex = 0
    for char, idx in key:
        if char == 'a':
            stringIndex += 1
            stringIndex *= idx

        if char == 'b':
            stringIndex += 2
            stringIndex *= idx

            # ... and so on

    return stringIndex


def myHash3(key, scrambleNumber):
    stringIndex = 0
    for char in key:
        if char == 'a':
            stringIndex += 1
            stringIndex *= scrambleNumber

        if char == 'b':
            stringIndex += 2
            stringIndex *= scrambleNumber

            # ... and so on

    return stringIndex

# How to reduce name collission?
# How to make the output more unique?
# How to make it non-invertible?
# How to make guessing the key, using the hash, really hard?
