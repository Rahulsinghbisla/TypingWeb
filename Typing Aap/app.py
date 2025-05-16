import random as r
from time import sleep

def cal_error(test, user):
    error = 0
    for i in range(min(len(test), len(user))):
        if test[i] != user[i]:
            error += 1
    error += abs(len(test) - len(user))
    return error

test = [ 
    "The quick brown fox jumps over the lazy dog.",
    "Success is not final; failure is not fatal: It is the courage to continue that counts.",
    "Artificial intelligence is transforming the world at an unprecedented pace.",
    "Persistence is the key to mastering any skill, including fast typing.",
    "Knowledge is power, but applying knowledge is true wisdom.",
    "In the world of coding, precision and logic are your best allies.",
    "A journey of a thousand miles begins with a single step.",
    "Focus on accuracy first, and speed will follow naturally.",
    "Reading and typing regularly are the best ways to improve your speed.",
    "Machine learning algorithms can be complex, but understanding them is rewarding."
]

test1 = r.choice(test)  # Get a single random string
print("Type the following sentence:")
print(test1)
print()

user = input("Enter: ")
print("Errors:", cal_error(test1, user))
