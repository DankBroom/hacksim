import random
import uuid
import time

def bF():
    a = 0
    while a < int(random.randint(5000, 29999)):
        id = str(uuid.uuid4())
        trimmed = id[:random.randint(0, len(id) - 1)]
        space = " " * random.randint(0, 15)
        print(f"{space}{trimmed}")
        a = a + 1
    
    print("###########################################################################")
    print("#  Password : " + trimmed)
    print("###########################################################################")

while True:
    time.sleep(1)
    b = input("[Hacker-Sim] > ")
    if b == "BrutForce":
        bF()
    elif b == "help":
        print("""
        ########### Hacker Sim ###########
            \n Les commandes :
        BruteForce > execute a brut force attack on a random ip
        help       > see this message""")