## 정렬
* 리스트의 원소들을 **특정 순서로 정리**하는 것
* 정렬 기준
    - 오름차순
    - 내림차순
    - 알파벳 순 
    - 등등
* 레코드들을 키값의 순서로 재배열하는 것
    - 레코드: 정렬시켜야 될 대상 (ex.학생)
    - 필드: 레코드를 작은 단위로 나눈 것 (ex.학번, 이름, 주소 등)
    - 키: 여러 필드 중에서 특별히 레코드와 레코드를 식별해주는 역할을 하는 필드 (ex.학번)
* 정렬 알고리즘을 평가하는 효율성의 기준
    - 정렬을 위해 필요한 **비교 연산의 횟수**
    - **이동 연산의 횟수**
* 정렬 알고리즘 분류(1)
    - 단순하지만 비효율적인 방법
        + 삽입 정렬, 선택 정렬, 버블 정렬 등
    - 복잡하지만 효율적인 방법
        + 퀵 정렬, 힙 정렬, 합병 정렬, 기수 정렬 등
* 정렬 알고리즘 분류(2)
    - 내부 정렬(internal sorting): 정렬하기 전에 모든 데이터가 메인 메모리에 올라와 있는 정렬을 의미
    - 외부 정렬(external sorting): 외부 기억장치에 대부분의 데이터가 있고, 일부만 메모리에 올려놓은 상태에서 정렬을 하는 방법
* 정렬 알고리즘 분류(3)
    - 안정성(stability): 입력 데이터에 동일한 키값을 갖는 레코드가 여러 개 존재할 경우, 이들 레코드들의 상대적인 위치가 정렬 후에도 바뀌지 않음 뜻한다.
    - 안정성 충족 정렬 알고리즘: 삽입 정렬, 버블 정렬, 합병 정렬 등

### 선택 정렬(Selection Sort)
* 리스트에서 가장 작은 값을 찾아서 0번 인덱스에 놓고, 두번째로 작은 값을 찾아서 1번 인덱스에 놓고 ...
* 즉, 각 위치에 어떤 값이 들어갈지 찾는다.
* 구현 방법
    - 두 개의 리스트 이용: 선택 정렬은 오른쪽 리스트에서 가장 작은 숫자를 선택하여 왼쪽 리스트로 이동하는 작업을 반복, 이것은 오른쪽 리스트가 공백 상태가 될 때까지 되풀이한다.
    - 한 개의 리스트 이용: 정렬이 안 된 리스트에서 최솟값이 선택되면 이 값을 배열의 첫 번째 요소와 교환한다. 이를 정렬이 될때까지 반복한다. = 제자리 정렬
    - 제자리 정렬: 입력 배열 이외에 다른 추가 메모리를 요구하지 않는 정렬 방법
* 단점 
    - 시간 복잡도: O(n**2) -> 효율적인 알고리즘은 아니다.
    - 안정성을 만족하지 않는다.
* 장점
    - 자료 이동 횟수가 미리 결정됨
    - 알고리즘이 매우 간단하다.
<br>

### 삽입 정렬(Insertion Sort)
* 각 값이 어떤 위치에 들어갈지 찾는다.
* 정렬이 되지 않은 부분의 숫자를 정렬된 부분의 적절한 위치에 삽입하는 과정을 반복한다.

#
### 개념 출처
* 온라인 코딩 강의 플랫폼 '코드잇' - 알고리즘 정석 강의
* C++로 쉽게 풀어쓴 자료구조