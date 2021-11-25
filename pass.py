import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBER = "0123456789"
Symbol = "!@#&?*._.,.,"

all= lower + upper + NUMBER + Symbol
lenght =  8
password = "".join(random.sample(all,lenght))
print(" The Password You Generated Is :",password)
