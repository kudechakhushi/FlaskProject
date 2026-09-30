import random
import string

import bcrypt

string_password = "admin12345"
print("string_password=", string_password)
salt = bcrypt.gensalt(rounds=12)
encoded_password = string_password.encode("utf-8")
print("encoded_password=", encoded_password)
hashed_login_password = bcrypt.hashpw(encoded_password, salt)
print("hashed_login_password=", hashed_login_password)
print("decode_hashed_login_password=", hashed_login_password.decode("utf-8"))

login_secretkey = ''.join(
    (random.choice(string.ascii_letters + string.digits)) for x in range(32))
print("login_secretkey=", login_secretkey)

user_str_password = "user12345"
print("user_str_password=", user_str_password)
user_byte_password = user_str_password.encode("utf-8")
print("user_byte_password=", user_byte_password)
db_str_password = "$2b$12$IH4EvIF5F6HfgrLHMZXMseAY8Q5PYtlGuVMSIHkMkRSgVvkMRf9Ye"
print("db_str_password=", db_str_password)
db_byte_password = db_str_password.encode("utf-8")
print(bcrypt.checkpw(user_byte_password, db_byte_password))
