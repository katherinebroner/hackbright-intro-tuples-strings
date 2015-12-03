def number_game():
	import random
	upper_bound = int(raw_input("Pick the upper bound on the range: "))
	random_number = random.randrange(1,upper_bound,1)
	guess_number = int(raw_input("Guess a number between 1 and %i! " % upper_bound)) 
	if guess_number > random_number:
		print "too high!"
	elif guess_number < random_number:
		print "too low!"
	else:
		print "you win!"
	print "the random number was %i" % random_number

number_game()
	
