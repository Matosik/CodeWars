def spoonerize(words):
    words_array=words.split(" ")
    one_word=list(words_array[0])
    two_word=list(words_array[1])
    tmp=one_word[0]
    one_word[0]=two_word[0]
    two_word[0]=tmp
    one_word="".join(one_word)
    two_word=''.join(two_word)
    ans=f"{one_word} {two_word}"
    return ans

a="красные яблоки"
print(spoonerize(a))


s = 'AABAABAAАA'
li = list(s)
li[5] = 'A'
result = ''.join(li)  # AABAAAAAАA