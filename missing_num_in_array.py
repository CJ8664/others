#!/usr/local/bin/python

# Problem Url: http://practice.geeksforgeeks.org/problems/missing-number-in-array/0

def input():
	return raw_input()

for i in range(int(input().strip())):
	num_ele = int(input().strip())
	print(str(((num_ele*(num_ele+1))/2)-sum(map(int, input().strip().split()))))