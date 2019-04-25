from random import choice, randint
import dictogram
import sampling
from pprint import pprint

def gen_markov(words):
  pairs = make_pairs(words.split(" "))
  markov_dict = {}
  for word1, word2 in pairs:
    if word1 in markov_dict:
      markov_dict[word1].add_count(word2)
    else:
      markov_dict[word1] = dictogram.Dictogram([word2])
  return markov_dict

def gen_sentence(chain ,num_words):
  word = list(chain.keys())[randint(0,len(chain.keys())-1)]
  return_sentence = ''
  for _ in range(num_words):
    return_sentence += ' ' + word
    word = sampling.sample(chain[word])
  return return_sentence



  





def make_pairs(corpus):
  output = []
  for i in range(len(corpus)-1):
    output.append((corpus[i],corpus[i+1]))
  return output

if __name__ == '__main__':
  chain = gen_markov("one fish two fish red fish blue fish blue")
  pprint(chain)
  print(gen_sentence(chain, 10))