import random
import string

all_symbols = string.ascii_letters + string.digits + string.punctuation

length = int(input('Choose your password length: '))

password = ''.join(random.sample(all_symbols, length))

print(password)
