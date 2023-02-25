import random
import time

count = 0
maxCount = 0
prize = random.randint(1000000,74000000)
ticketPrice = 3
ticketPrices = 0

ticketsAmount = int(input("Please enter an amount of lottery tickets to buy: "))

ticketPrices = ticketsAmount * ticketPrice

time.sleep(1)

print("You bought " + str(ticketsAmount) + " tickets, which cost you £" + str(ticketPrices) + ". The prize is worth £" + str(prize) + ".")

print(" ")
print(" ")
print(" ")

time.sleep(5)

print("Running...")
while True:
    if ticketsAmount == 0:
        print("You ran out of tickets and didn't win!")
        break
    count += 1
    ticketsAmount -= 1
    print(str(count))
    a = random.randint(1,50)
    b = random.randint(1,50)
    c = random.randint(1,50)
    d = random.randint(1,50)
    if a == b and b == c and c == d:
                print("WIN!!! Took " + str(count) + " attempts. You spent £" + str(ticketPrices) + " on tickets, and won £" + str(prize) + "!")
                break
    

    
