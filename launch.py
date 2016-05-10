launch = int(input("Time for launch off: "))
print("Launch off beggining...")
i = launch
while i > 0:
    print(i,"...") 
    i = i - 1
    print("Lift off!")
print("We are now entering outer space. Congrats team, you guys did an excuisit job.")
planet = input("What planet would you like to go to? ")
if 'moon' in planet.lower():
    print("The Moon is 238,900 miles away! It can be alittle cold reaching -387 degrees.")
if 'jupiter' in planet.lower():
    print("Jupiter is 628,743,036 miles away! It can reaach up to -234 degrees. Might want to wear a couple layers.")
if 'mars' in planet.lower():
    print("Mars is 249,000,000 miles away! It's usually 70 degrees so nothing to worry about.")
if 'uranus' in planet.lower():
    print("Uranus is 1.6,000,000,000 miles away! It reaches -357 degrees! You might want to bring a coat.")
if 'sun' in planet.lower():
    print("The Sun is 92.96,000,000 miles away! May I recommend to wear a pair of sunglasses if you really do decide to go!")

    


