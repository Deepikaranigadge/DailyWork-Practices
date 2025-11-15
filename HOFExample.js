//map()=======

const numbers = [1, 2, 3, 4];
const doubled = numbers.map(num => num * 2);
console.log(doubled);

//filter()======

const numbers1 = [1, 2, 3, 4, 5, 6];
const evens = numbers1.filter(num => num % 2 === 0);
console.log(evens);

//reduce()=======
const numbers2 = [1, 2, 3, 4];
const sum = numbers2.reduce((acc, curr) => acc + curr, 0);
console.log(sum);

