
def get_cs():
  cs=input("Enter the string :")
  return cs


def cs_to_lot(cs):
  lot=list()
  lot=cs.split()
  return lot


def main():
  cs = get_cs()
  lot = cs_to_lot(cs)
  print(lot)


if __name__ == '__main__':
  main()  
