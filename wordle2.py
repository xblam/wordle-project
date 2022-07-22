def check_answer(word,guess):
    result = ''
    for i in range(len(word)):
        if word[i]==guess[i]:
            result+=word[i]
        else:
            result+='*'
    if result == word:
        return True
    else:
        return False


print(check_answer('bench','danch'))
