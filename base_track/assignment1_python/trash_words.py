def process(sentences):
    result = []
    for sentence in sentences:
        words = sentence.split()
        preresult = []
        for word in words:
            word_filtered = "".join([char for char in word if char.isalpha()])
            if word_filtered == word:
                preresult.append(word_filtered)
        result.append(" ".join(preresult))
    return result

lst = ['1 thousand devils', 'My name is 9Pasha', 'Room #125 costs $100', '888']
print(process(lst))