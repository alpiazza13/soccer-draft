def all_subwords(word):
    subwords = []
    length = len(word)
    i = 0
    while i < length:
        j = i+1
        while j <= length:
            subword = word[i:j]
            subwords.append(subword)
            j += 1
        i += 1
    return subwords

#str1 should be the real player
#determines whether at least 1/3 of the substrings of str1 are in str2
# maybe convert to lowercase first
# determines: whether str2 is similar to str1
def is_similar(str1, str2):
    # too_long = len(str2) > 1.5*len(str1)
    # if too_long:
    #     return False
    count = 0
    sub1 = all_subwords(str1)
    for word in sub1:
        if word in str2:
            count += 1
    minimum = len(sub1) / 3
    if count >= minimum:
        return True
    return False


print(is_similar("Marcel", "Marseille"))
print(is_similar("Marseille", "Marcel"))
