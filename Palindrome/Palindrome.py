def is_palindrome(word):
    # 코드를 입력하세요.
    index = len(word) - 1
    for spell in word:
        if spell != word[index]:
            return False
        index -= 1
    return True


# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))