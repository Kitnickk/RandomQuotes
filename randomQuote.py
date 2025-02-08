import time, random

v = False

quotes = [
    "One day you'll make it. Today might be that day",
    "Success is not final, failure is not fatal: It is the courage to continue that counts",
    "The only way to do great work is to love what you do.",
    "You miss 100percent of the shots you don't take.",
    "It does not matter how slowly you go as long as you do not stop.",
    "The greatest glory in living lies not in never falling, but in rising every time we fall.",
    "Don't let what you cannot do interfere with what you can do."
]

for i in quotes:
    print(random.choice(quotes))
    time.sleep(3)