#find the oldest and youngest pupil in the class of 4, namely:Sharon, John,Grace,Emmanuel.
#Sharon is 12years old, John is 7 years old, Grace is 10 years old and Emmanuel is 6years old.s
def biggest(a,y,z,w):
	
	Max = a
	if y > Max:
		Max = y

	if z > Max:
		Max = z

	if w > Max:
		Max = w

	return Max

print(biggest(10,7,6,12))

def smallest(a,b,c,d):
	Min = c

	if a < Min:
		Min = a

	if b < Min:
		Min = b

	if d < Min:
		Min = d

	return Min

print(smallest(7,6,10,12))


def show_age():
	data =("sharon",12, "John",7, "Grace",10, "Emmanuel",6)
	print ("%s is %d years old,%s is %d years old,%s is %d years old and %s is %d years old.Sharon is the oldest while Emmanuel is the youngest." % data)

print(show_age())