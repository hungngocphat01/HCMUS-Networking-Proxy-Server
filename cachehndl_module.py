import hashlib

def md5(string):
    return hashlib.md5(string.encode("UTF-8")).digest()

# Insert your functions here
