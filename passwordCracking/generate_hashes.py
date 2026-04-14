import hashlib


# Takes a string and turns it into a hash using sha256
# To use and make your own just replace password string and run program
# ---------------------------------------------------------------------

password = "i_love_dogs"
hash = hashlib.sha256(password.encode('utf-8'))
print(hash.hexdigest())