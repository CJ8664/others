#!/usr/local/bin/python

# Problem URL : https://code.google.com/codejam/contest/6254486/dashboard#s=p1

decider = 1

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
		counter = 0

		while(sum(input_stack) != len(input_stack) and sum(input_stack) != 0 ):
			decider = input_stack[i]
			#print (i,decider,input_stack)
			while( i >= 0 ):
				if(input_stack[i] == decider): # Already is a happy face do nothing
					i -= 1
					continue
				else:
					temp_stack = ([ (x+1)%2 for x in input_stack[:i+1]])[::-1]
					mans +=1
					input_stack = temp_stack + input_stack[i+1:]
					break

			if (i<0):
				i = len(input_stack) - 1

		if(sum(input_stack) == 0):
			return mans+1
		else:
			return mans

def main():

	global mans, decider

	input_handle = open('B-large-practice.in','r')

	num_test_cases = int(input_handle.readline().strip())

	for test_case in xrange(1, num_test_cases+1):

		input_stack = [ 1 if x == '+' else 0 for x in input_handle.readline().strip()]

		decider = input_stack[-1]

		mans = getNumberOfManeuver(input_stack)
		print('Case #' + str(test_case) + ': ' + str(mans))

	input_handle.close()

if __name__ == '__main__':
	main()