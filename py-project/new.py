def river_cross(supplies,people):
	'''Checks to see if river crossing is successful.'''
	import random
	depth=(random.randint(2,10))
	width=(random.randint(100,300))
	chance=(width*depth/3000*100)
	success=(random.randint(1,100))
	print('The river is',depth,
      'feet deep at its deepest point, and',
      width,'feet accross.  You have a', chance,
      '% chance of crossing successfully.')
	choice = input('''You must choose how to cross:
		1.  Attempt to ford the river.
		2.  Caulk the wagon and float it accross.
		3.  Wait to see if conditions improve.
		What is your choice? ''')
	if choice == '1':
		print('You attempt to ford the river')
		if (success) <= (chance):
			return True
		else:
			return False
	elif choice == '2':
		# day = day +1
		print('You spend a day caulking the wagon and attempt to float accross.')
		(success)=((success)*2)
		if (success) <= (chance):
			return True
		else:
			return False
	elif choice == '3':
		# day = day +1
		print('You wait a day to see if conditions improve.')
		print('')
		return river_cross(supplies,people)
	else: 
		return 'Please choose 1, 2, or 3.'


