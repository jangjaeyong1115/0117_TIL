def count(word,char):
    total = 0

    for i in word:
        if i == char:
            total = total + 1

    return total