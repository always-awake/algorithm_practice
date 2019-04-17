## 알고리즘이란?
### 알고리즘이란?
* 알고리즘이란, 어떤 문제를 해결하기 위한 자세한 방법
* 같은 문제를 해결하기 위해서도 다양한 알고리즘이 존재
* 프로그래밍을 이용해 알고리즘 구

### 좋은 알고리즘이란?
* 문제를 해결하는 알고리즘
* 문제를 더 잘 해결하는 알고리 (효율적, 짧은 시간)

### 컴퓨터 알고리즘이란?
* 컴퓨터가 어떤 문제를 해결하기 위해서 컴퓨터가 이해할 수 있는 방식으로 정리되어 있는 해결 방법

## 탐색
* 저장된 정보들 중에서 **원하는 값**을 찾는 것
* 선형 탐색 알고리즘(linear search algorithm)
    - 데이터가 모인 집합(list, linked list etc)의 처음부터 끝까지 하나씩 순서대로 비교하며 원하는 값을 찾아내는 알고리
    - Linked List에서 자주 쓰이는 알고리즘
    - 가장 짧은 시간이 걸리는 경우: 원하는 값이 정보들의 가장 앞에 있을 경우
    - 가장 오랜 시간이 걸리는 경우: 원하는 값이 정보들의 가장 뒤에 있을 경우(모든 데이터들 확인하고 비교해야함)
* 이진 탐색 알고리(binary search algorithm)
    - 정렬된 데이터가 모인 집합의 중간값부터 탐색
    - 정렬된 데이터가 아니면 적용이 불가능한 알고리즘
    - 1회 비교를 거칠 때마다 탐색 범위가 (대략)절반으로 줄어든다.
    - 트리 구조에서 자주 쓰는 알고리즘
### 탐색 알고리즘 비교
<img src="./images/스크린샷 2019-04-17 오후 5.08.57.png" />
* 정렬 된 리스트 
    - 선형 탐색(O)
    - 이진 탐색(O)
* 정렬이 안된 리스트
    - 선형 탐색(O)
    - 이진 탐색(X)
* 선형 탐색이 쓸모 없는 것은 아님!

## 정렬
* 리스트의 원소들을 **특정 순서로 정리**하는 것
* 정렬 기준
    - 오름차순
    - 내림차순
    - 알파벳 순 
    - 등등
### 선택 정렬(Selection Sort)
* 리스트에서 가장 작은 값을 찾아서 0번 인덱스에 놓고, 두번째로 작은 값을 찾아서 1번 인덱스에 놓고 ...
* 즉, 각 위치에 어떤 값이 들어갈지 찾는다.

### 삽입 정렬(Insertion Sort)
* 각 값이 어떤 위치에 들어갈지 찾는다.
