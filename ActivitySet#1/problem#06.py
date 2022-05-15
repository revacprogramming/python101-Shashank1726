# Loops & Iterators

largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        num = int(num)
        largest = num if largest is None or largest < num else largest
        smallest = num if smallest is None or smallest > num else smallest
            
    except ValueError:
        print("enter numbers only")

print ("Maximum", largest)
print ("Minimum", smallest)