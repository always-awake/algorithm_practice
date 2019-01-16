# input: "USA", "FlaG" ...
# output: Bool

class Solution:
    def detectCapitalUse(self, word):
        
        word = list(word)
        
        for i in range(0, len(word)):
            if word[i].isupper():
                word[i] = True
            else:
                word[i] = False
        
        # 모든 문자가 대문자일 경우
        if word.count(True)==len(word):
            return True
        # 모든 문자가 소문자일 경우
        elif word.count(True)==0:
            return True
        # 문자열의 첫 문자가 대문자일 경우
        elif word.count(True)==1 and word[0] is True:
            return True
        # 위 3경위 외에는 모두 False
        else:
            return False