import random
r = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
w = input('Enter the word to Coded into secret language : ')

if len(w) >= 3 :
    word = w.lstrip()[1:] + w.rstrip()[:1]
    r_word = random.sample(r,3)
    nr_word = ''.join(r_word)
    n_word = nr_word + word + nr_word
    print(f'The secret word is :{n_word}')

else :
    word = w.lstrip()[1:] + w.rstrip()[:1]
    print(f'The secret word is :{word}')