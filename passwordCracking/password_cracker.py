import hashlib
user_hash_dict = {}


# Getting a list of common passwords from the txt file
# ----------------------------------------------------------
with open('passwordCracking/common_passwords.txt', 'r') as f:
    common_passwords = f.read().splitlines()


# Getting a list of usernames and hashed passwords
# ----------------------------------------------------------
with open('passwordCracking/username_hashes.txt', 'r') as f:
    text = f.read().splitlines()
    for user_hash in text:
        username = user_hash.split(":")[0]
        hash = user_hash.split(":")[1]
        user_hash_dict[username] = hash


# Hash your list of known passwords and then cheack each of 
# them to see if they match the hashes you have.
# ----------------------------------------------------------
for password in common_passwords:
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    for username, hash in user_hash_dict.items():
        if hashed_password == hash:
            print(f'HASH FOUND\n{username}:{password}')