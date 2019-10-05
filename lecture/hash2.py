import time
import hashlib
import bcrypt

# hashlib.sha256

n = 50
key = "mykey"

start_time = time.time()
for i in range(n):
    hashlib.sha256(key)

end_time = time.time()
print('sha256 runtime: ', end_time - start_time)

salt = bcrypt.gensalt()

start_time = time.time()
for i in range(n):
    bcrypt.hashpw(key, salt)
end_time = time.time()

print("bcrypty runtime: ", end_time - start_time)
