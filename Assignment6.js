//HOF using map() method

const nums = [1, 2, 3];
const doubled = nums.map(n => n * 2);
console.log(doubled); // [2, 4, 6]

//HOF using filter() method
const nums1 = [1, 2, 3, 4];
const evens = nums1.filter(n => n % 2 === 0);
console.log(evens); // [2, 4]

//HOF using reduce() method
const nums3 = [1, 2, 3, 4];
const sum = nums3.reduce((t, n) => t + n, 0);
console.log(sum); // 10

//HOF using find() method
const nums4 = [10, 20, 30];
const found = nums4.find(n => n > 15);
console.log(found); // 20

//HOF using findIndex() method
const nums5 = [5, 10, 15];
const index = nums5.findIndex(n => n === 10);
console.log(index); // 1

//HOF using some() method
const nums6 = [1, 3, 5];
console.log(nums6.some(n => n % 2 === 0)); // false

//HOF using () method
const nums7 = [2, 4, 6];
console.log(nums7.every(n => n % 2 === 0)); // true
