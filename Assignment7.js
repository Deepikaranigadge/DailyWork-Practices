//HOF using sort() method

const nums = [4, 1, 3, 2];
nums.sort((a, b) => a - b);
console.log(nums); // [1,2,3,4]

//HOF using flatmap() method

const arr = [1, 2, 3];
const output = arr.flatMap(n => [n, n * 2]);
console.log(output); // [1,2,2,4,3,6]

//HOF using foreach() method

const nums1 = [1, 2, 3];
nums.forEach(n => console.log(n));