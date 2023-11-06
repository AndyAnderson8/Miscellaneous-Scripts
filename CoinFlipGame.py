import random

correctGuesses = 0
incorrectGuesses = 0

while True:
  percentHeads = random.randrange(1, 101)
  if percentHeads < 50:
    percentHeads = 50

  headCount = 0
  tailCount = 0

  guessed = False

  print("\n" + str(correctGuesses) + " wins | " + str(incorrectGuesses) + " losses \n-----------------")

  while guessed == False:
    value = random.randrange(1, 101)
    if value >= percentHeads:
      tailCount += 1
    else:
      headCount += 1
    
    print("Heads: " + str(headCount) + " | Tails: " + str(tailCount))
    
    inputVar = input("Enter selection (f, c, t): ")
    print()

    if inputVar == "c":
      if percentHeads > 50:
        print("Correct! Coin was rigged! (" + str(percentHeads) + "%)")
        correctGuesses += 1
      else:
        print("Wrong! Coin was not rigged! (" + str(percentHeads) + "%)")
        incorrectGuesses += 1
      guessed = True
    
    elif inputVar == "t":
      if percentHeads > 50:
        print("Wrong! Coin was rigged! (" + str(percentHeads) + "%)")
        incorrectGuesses += 1
      else:
        print("Correct! Coin was not rigged! (" + str(percentHeads) + "%)")
        correctGuesses += 1
      guessed = True







  

