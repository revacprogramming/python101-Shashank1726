# Variables, Expressions & Statements

def Earning(hrs,rate):
  wage = hrs*rate
  return wage

	
def output(wage):
	print("Earning",wage)

	
def main():
	hrs=float(input("Enter hours:"))
	rate=float(input("Enter rate:"))
	wage=Earning(hrs,rate)
	output(wage)

	
main()	