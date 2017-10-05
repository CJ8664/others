#!/usr/local/bin/python

# Problem URL : http://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0

def input():
	return raw_input()

for i in range(int(input().strip())):
	
	expected_sum = int(input().strip().split()[1])
	curr_sum = i = j = 0
	input_arr = [int(x) for x in input().strip().split()]

	for num in input_arr:
		curr_sum += num
		while curr_sum > expected_sum:
			curr_sum -= input_arr[i]
			i += 1
		if curr_sum == expected_sum:
			j+=1
			break
		j +=1
	if curr_sum == expected_sum:
	    print('{} {}'.format(i+1,j))
	else:
	    print('{}'.format(-1))