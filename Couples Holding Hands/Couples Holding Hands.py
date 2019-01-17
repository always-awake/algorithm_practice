class Solution:
    def minSwapsCouples(self, row):
        
        count = 0
        left = 0
        right = 1
        
        while row:  
            
            #커플인 경우 1: 첫 번째 사람이 짝수인 경우
            if row[left] % 2 == 0 and row[right]-row[left] == 1:
                row.pop(left)
                row.pop(0) 
            #커플인 경우 2: 첫 번째 사람이 홀수인 경우
            elif row[left] % 2 == 1 and row[left] - row[right] == 1:
                row.pop(left)
                row.pop(0)   
            
            #커플이 아닌 경우
            else:
                #첫 번째 사람이 짝수인 경우
                if row[left] % 2 == 0:        
                    while row[right] - row[left] != 1:
                        right = right + 1
                #첫 번째 사람이 홀수인 경우
                if row[left] % 2 == 1:
                    while row[left] - row[right] != 1:
                        right = right + 1
                        
                #row[0]의 짝을 찾으면, row[1]과 자리 바꾸기       
                row[left+1], row[right] = row[right], row[left+1]                
                count = count + 1
                
                row.pop(left)
                row.pop(0)
                
                #right값 초기화
                right = 1
        return count
         