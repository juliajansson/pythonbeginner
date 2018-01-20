import math

pi=math.pi
print("This is a test on a Raspberry " + str(pi) + " computer!")

a=input("Now, you may wonder how pi pis look? (Answer with [y] or [n].) ")

if a == "y":
	lotsofpis=str(math.pi) * int(math.pi)
	print(lotsofpis)

else:
	print("Whatever, I can't show you anyway, since python can't handle an infinite amount of digits... Also it would be difficult to represent a non integer amount of numbers.")

i=input("Now enter an integer. ")

#Can't handle negative numbers atm

k=0
x=1
if i < 0:
	while k>i:
		x=x/2
		k-=1
elif i==0:
	x=x
else:
	while k<i:
		x=2*x
		k+=1

print(str(x))
