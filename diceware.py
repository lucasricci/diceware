import secrets
import os

rng = secrets.SystemRandom()
dir = os.path.dirname(__file__)
dw = open(f"{dir}/eff_large_wordlist.txt", "r")
dw_dict = {}

for line in dw:
    k, v = line.split()
    dw_dict[int(k)] = v

number_words = int(input("How many words you want? "))
randlist = []

for n in range(number_words):
    number = ""
    for m in range(5):
        byte = rng.randint(1, 6)
        number += str(byte)
    randlist.append(int(number))

for x in randlist:
    word = dw_dict.get(x)
    print(word, end=" ")
