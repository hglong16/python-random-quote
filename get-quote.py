import random
def main():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes)
  last = len(quotes) - 1
  rnd = random.randint(0, last)
  print(quotes[rnd])
if __name__== "primary":
  main()
