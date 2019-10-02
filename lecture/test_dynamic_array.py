
import time

n = 10000000

start_time = time.time()

myarray = []
for num in range(n):
    myarray.append(num)

end_time = time.time()
print("Append test took: ", end_time - start_time)


# start_time = time.time()
# myarray = []

# for num in range(n):
#     myarray.insert(0, num)

# end_time = time.time()
# print("Insert test took: ", end_time - start_time)


myarray = [None] * n
start_time = time.time()
myarray = []
for num in range(n):
    myarray.append(num)
end_time = time.time()
print("this preallocation append took: ", end_time - start_time)
