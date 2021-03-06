#!/usr/local/bin/python

# Problem URL : https://code.google.com/codejam/contest/6254486/dashboard#s=p1

def getNumberOfManeuver(input_stack):

	# Variable that stores the number of maneuvers
	mans = 0

	if(input_stack == [1]): # Base case No maneuvers required
		return 0
	elif (input_stack == [0] or input_stack == [0, 1]): # Base case 1 maneuver required
		return 1
	elif (input_stack == [1, 0]): # Base case 2 maneuver required
		return 2
	# Perform maneuver
	else:
		i = len(input_stack) - 1

		while( i>=0 ):
			if(input_stack[i] == 1): # Already is a happy face do nothing
				i -= 1
				continue
			else:
				break	

		if( i > 0): # Perform Maneuver
			new_stack = ([ (x+1)%2 for x in input_stack[:i+1]])[::-1] # Filp and reverse	
			if ( new_stack != [1, 0] and new_stack != [0, 1]):
				mans += 1
			mans += getNumberOfManeuver(new_stack)

	return mans

def main():

	global mans

	input_handle = open('B-small-practice.in','r')

	num_test_cases = int(input_handle.readline().strip())

	for test_case in xrange(1, num_test_cases+1):

		input_stack = [ 1 if x == '+' else 0 for x in input_handle.readline().strip()]

		mans = getNumberOfManeuver(input_stack)
		print('Case #' + str(test_case) + ': ' + str(mans))

	input_handle.close()

if __name__ == '__main__':
	main()