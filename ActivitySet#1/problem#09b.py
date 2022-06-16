#Lists
def myinput():    
    fhand = open("dataset/mbox-short.txt")
    return fhand

def counts(fhand):    
    count=0
    for line in fhand:
      if line.startswith('From '):
        words = line.split()                     
        print(words[1])                       
        count = count + 1
    return count    

def output(count):    
    print ("There were", count, "lines in the file with From as the first word")

  def main():
    fhand=myinput()
    count=counts(fhand) 
    output(count)

main()
