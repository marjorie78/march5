sentence=input("give me a sentence")
number_words=0
for letter in sentence:
    if letter==" ":
        number_words=number_words+1
print("there are",number_words+1,"words")