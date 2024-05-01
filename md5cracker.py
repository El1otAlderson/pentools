import hashlib
import sys



wordlist_location = sys.argv[1] 
hash_input = sys.argv[2]

if len(sys.argv) != 3:   #IF statement checks that is user properly used the command | 3 because we have 3 sys.argv  first is 0 for the whole program   second is 1 for wordlist and third is 2 for hash input 
    print("Usage: python md5cracker.py <wordlist> <hash_input in md5> ")
    sys.exit(1)


with open(wordlist_location, 'r') as file:  #File opening
    for line in file.readlines():  #Read all lines from the file and iterate through them
        hash_ob = hashlib.md5(line.strip().encode()) #Creating md5 hash of the plain text 
        hashed_pass = hash_ob.hexdigest() #Converting created hash to hexdecimal
        if hashed_pass == hash_input: #Checks that hash we created is the same like we wanted to crack 
            print('Found cleartext password! ' + line.strip())
            exit(0)
print("Password not found try another wordlist")
