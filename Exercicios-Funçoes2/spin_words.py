def spin_words(sentence):
    new_sentence = sentence.split()
    sentence = '' #Zerando o parametro sentence
    cont = 0
    for p in new_sentence:
        if len(p) >= 5:
            #Se a palavra tiver mais de 5 letras, substutiuir ela por ele mesma invertida -> Another : rehtonA
            new_sentence[cont] = p[::-1]
        cont+=1
    sentence = ' '.join(new_sentence)
    return sentence

teste1 = spin_words("This sentence is a sentence")
teste2 = spin_words("This is a another test")
teste3 = spin_words("Hey fellow warriors")
teste4 = spin_words("Welcome")
print(teste1)
print(teste2)
print(teste3)
print(teste4)
