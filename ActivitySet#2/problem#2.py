def input_two_numbers():
    a = input("Enter the first number :- ")
    b = input("Enter the second number :- ")
    return a,b
def add(a, b):
    c = float(a)+float(b) 
    return c
def output(a, b, sum_):
    print("The sum of ",a ,"and", b ,"is",sum_)  
def main():
    a, b = input_two_numbers()
    res = add(a, b)
    output(a, b, res)

if __name__ == '__main__':
    main()