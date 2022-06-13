# Conditional Execution

def computation(h,r):
	if h <= 40:
	 	return h*r
	elif h > 40:
		return 40*r+(h-40)*1.5*r

		
def output(wage):
	print ("Earing",wage)

	
def main():
	hours=float(input("Enter Hours:"))
	rate= float(input("Enter the Rate:"))
	wage=computation(hours,rate)
	output(wage)

	
main()	
