import sys
import random

def reaarrange(words):
  for x in range(random.randint(1,len(words)*2)):
    pos1 = random.randint(0,len(words)-1)
    pos2 = random.randint(0,len(words)-1)
    words[pos1], words[pos2] = words[pos2], words[pos1]
  return(words)

if __name__ == '__main__':
  l = sys.argv[1:]
  print(reaarrange(l))