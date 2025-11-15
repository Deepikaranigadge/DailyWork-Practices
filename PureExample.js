//Pure Function ======

function add(a, b) {
  return a + b;
}

console.log(add(2, 3)); // 5
console.log(add(2, 3)); // 5 (same input = same output)

//CallBack function======

function greet(name) {
  console.log("Hello, " + name);
}

function processUserInput(callback) {
  const userName = "Deepika";
  callback(userName); // calling the callback function
}

processUserInput(greet);

//currying function =======

function add(a, b, c) {
  return a + b + c;
}

console.log(add(1, 2, 3)); // 6

// Factorial
function factorial(n) {
  // Base condition (must needed)
  if (n === 1) {
    return 1;
  }

  // Recursive call
  return n * factorial(n - 1);
}
console.log(factorial(5)); // 120


