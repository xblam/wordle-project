def check_answer(word,guess):
    result = ''
    for i in range(len(word)):
        if word[i]==guess[i]:
            result+=word[i]
        else:
            result+='*'
    return result


print(check_answer('bench','danch'))
