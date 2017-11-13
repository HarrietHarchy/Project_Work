#To create a prime number generator:
# To give the first a hundred prime numbers.
for i in range(2,100):
#supposing i variable has numbers, 3,11,23,29...43;
#then j=2++, 

	j=2
	counter = 0

	while j<i:
				if i%j == 0:
						counter=1
						j=j+1
				else:
					j=j+1
	if counter == 0:
		print(str(i)+ " is a prime number")

	else:
		 counter = 0

