#!/usr/local/bin/python

# Program URL : http://practice.geeksforgeeks.org/problems/is-binary-number-multiple-of-3/0

def input():
	return raw_input()

def bin_to_int(str):
	#print('Converting: {}'.format(str))
	max_power = len(str) - 1
	int_num = 0

	for bit in str:
		if bit == '1':
			int_num += (2**max_power) 
		max_power -=1

	#print('Integer: {}'.format(int_num))
	return int_num

for case in range(int(input().strip())):
	
	# Read input binary string 
	bin_str = input().strip()

	remainder = ''
	i = 0

	while i < len(bin_str):
		remainder += bin_str[i:i+1]

		bin_int = bin_to_int(remainder)

		if bin_int < 3:
			i+=1
			continue
		else:
			remainder = bin_int - 3

			if remainder == 0:
					remainder = ''
			elif remainder == 1:
				remainder = '1'
			else:
				remainder = '10'
			i+=1


	if bin_to_int(remainder) == 0:
		print('1')
	else:
		print('0')



