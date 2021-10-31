import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@$_"
total = lower + upper + numbers + symbols
length = 8
password = "".join(random.sample(total, length))
print(password)