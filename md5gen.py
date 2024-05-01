import hashlib
import sys 

plaintext = sys.argv[1]

if len(sys.argv) != 2:  
    print("Usage: python md5gen.py plaintext ")
    sys.exit(1)

hash_ob = hashlib.md5(plaintext.encode())
hashed_pass = hash_ob.hexdigest()
print(hashed_pass)
