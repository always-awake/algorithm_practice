const swap = (targetArray, currentIndex, cur, next) => {
    targetArray[currentIndex] = next;
    targetArray[currentIndex+1] = cur;
};

const bubbleSorting = (numbers) => {
    const newNumbers = numbers.slice();
    const length = numbers.length;
    let isSwap = false;
    
    for (let i = length - 1; i > 0; i--) {
        for (let j = 0; j < i; j ++) {
            let cur = newNumbers[j];
            let next = newNumbers[j + 1];

            if (cur > next) {
                isSwap = true;
                swap(newNumbers, j, cur, next,);
            }
        }
        if (!isSwap) return newNumbers; // 원소 간 swap이 발생하지 않은 최선의 경우
    }

    return newNumbers;
};  


// test
const numbers = [8, 4, 9, 2, 5, 10, 15, 22, 88, 63, 18];
console.log(bubbleSorting(numbers)); // [2, 4, 5, 8, 9, 10, 15, 18, 22, 63, 88]

const numbers2 = [7, 4, 5, 1];
console.log(bubbleSorting(numbers2)); // [ 1, 4, 5, 7 ]