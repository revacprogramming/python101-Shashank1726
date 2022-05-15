# Lists

fname = input("Enter the file name")
fhand = open(fname)
mylist = list()
for line in fhand:
    l=line.split()
    for i in l:
    	if i not in mylist:
        	mylist.append(i)
mylist.sort()
print(mylist)
