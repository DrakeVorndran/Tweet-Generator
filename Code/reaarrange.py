import sys
import random

def reaarrange(words):
  for x in reversed(range(1,len(words))):
    pos = random.randint(0,x-1)
    words[x], words[pos] = words[pos], words[x]
  return(words)

def reverseString(string, seperator=""):
  if(seperator == ""):
    return_string = list(string)
    
  else:
    return_string = string.split(seperator)
  return_string.reverse()
  return return_string

def anagram(word):
  return "".join(reaarrange(list(word)))


if __name__ == '__main__':
  l = sys.argv[1:]
  print(reaarrange(l))
  # print(reverseString("hello my name is bob", " "))
  # print(anagram("anagram"))