#!/usr/bin/env python

import numpy as np

def main():
	theta = np.loadtxt("theta.csv", dtype = np.longdouble)
	try:
		x = np.longdouble(raw_input("Enter a mileage: "))
	except:
		print ("Error happens")
		exit()
	if x < 0:
		print ("mileage cannot be less then 0")
		exit()
	print ("Predicted  price is:")
	if x > theta[2]:
		print ("Such old crap has value NULL!!! Maximum mileage is")
		print theta[2]
	else:
		print theta[0] + theta[1] * x

if __name__ == "__main__":
	main()
