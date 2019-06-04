# 프로그래머스 완전탐색 - 카펫 문제

## 문제 설명
# Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 빨간색으로 칠해져 있고 모서리는 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.
# Leo는 집으로 돌아와서 아까 본 카펫의 빨간색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.
# Leo가 본 카펫에서 갈색 격자의 수 brown, 빨간색 격자의 수 red가 매개변수로 주어질 때 카펫의 가로, 
# 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

## 제한사항
# 갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
# 빨간색 격자의 수 red는 1 이상 2,000,000 이하인 자연수입니다.
# 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, red):
    factor = []
    i = 1
    # red 약수 구하기
    while True: 
        if i > red/i: 
            break
        if red % i == 0:
            factor.append([int(red/i), i])
        i += 1
    for j in factor:
        if ((j[0]*2) + (j[1]*2) + 4) == brown:
            answer = [j[0]+2, j[1]+2]
    return answer