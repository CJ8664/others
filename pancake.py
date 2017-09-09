#!/usr/local/bin/python

# Problem URL : https://code.google.com/codejam/contest/6254486/dashboard#s=p1

def performManeuver(small_stack):

	#print('performManeuver input: ' + str(small_stack))

	new_small_stack = ([ (x+1)%2 for x in small_stack])[::-1]

	#print('performManeuver output: ' + str(new_small_stack))
	return new_small_stack

def getNumberOfManeuver(input_stack):

	mans = 0
	i = len(input_stack) - 1

	decider = input_stack[-1]

	while( i>=0 ):
		if(input_stack[i] == decider): # Already is a happy face do nothing
			i -= 1
			continue
		else: # Perform Maneuver
			new_stack = performManeuver(input_stack[:i+1])
			mans +=1
			input_stack = new_stack + input_stack[len(new_stack)-1:] # Redefine the input for next iteration

	if (decider == 0):
		return mans + 1
	return mans

def main():

	for test_case in xrange(1, int(raw_input()) + 1):

		input_stack = [ 1 if x == '+' else 0 for x in raw_input()]

		#print(str(input_stack))

		mans = getNumberOfManeuver(input_stack)
		print('Case #' + str(test_case) + ': ' + str(mans))

if __name__ == '__main__':
	main()