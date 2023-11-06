trials = 10000 # 10,000 trials for each

import random   # Just getting the python code set up for these lines
completedTrials = 0 
switchWins = 0
originalWins = 0

while completedTrials != 2*trials: # want to run 20,000 trials total before calculations (10,000 for original, 10,000 for switch)
	pickedDoor = random.randint(1, 3) # picked door is random integer 1 - 3
	correctDoor = random.randint(1, 3) # prize door is random integer 1 - 3 too

	if completedTrials > trials:   #for first 10,000 trials, use original door.
		if pickedDoor == correctDoor:
			originalWins = originalWins + 1  # if the picked door is the prize door, +1 win is logged for original door strategy. 
	else: # the next 10,000 trials are for the switched door
		revealDoor = [1, 2, 3]   
		revealDoor.remove(correctDoor)  #they wont reveal the correct door, so remove that from possibilities
		if pickedDoor == correctDoor:
			revealDoor.remove(revealDoor[random.randint(0, 1)]) #if the original door is already the prize door, just show a random losing door from the two
		else:
			revealDoor.remove(pickedDoor) # if not, you have to remove the picked door too as its not the same thing
		revealDoor = revealDoor[0]

		switchedDoor = [1, 2, 3]
		switchedDoor.remove(revealDoor) # cant switch to the revealed door
		switchedDoor.remove(pickedDoor) #its not a switch if you stay with your original door
		switchedDoor = switchedDoor[0]

		if switchedDoor == correctDoor:
			switchWins = switchWins + 1 #if the switched door was the winning door, + 1 win is logged for switched door strategy
		
	completedTrials = completedTrials + 1  # log a completed trial
	
if switchWins > originalWins:
	print("Switch wins!")
else:
	print("Original wins!")
print(100*switchWins/trials, "% switch winrate -", 100*originalWins/trials, "% original winrate")  #calculate win percentage for each and display the winner