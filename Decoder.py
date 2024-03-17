w = input('Enter the encoded word : ')

if len(w) >= 3 :
    word = w[3:]
    n_word = word[:-3]
    d_word = n_word[-1] + n_word[:-1]
    print(n_word)
    print(d_word)

else :
    word = w[-1] + w[:-1]
    print (word)