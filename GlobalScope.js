// Global variable=======

//var name = "Deepika";
//function showName() {
  //console.log(name); 
//}
//showName(); 
//console.log(name); 



//Function Scope========
//function testFunction() {
  //let message = "Hello, I am inside the function!";
  //console.log(message); //Accessible here
//}
//testFunction();
//console.log(message); // Error: message is not defined




//BlockScope =========
{
  let a = 10;
  const b = 20;

  console.log(a); // ✅ 10
  console.log(b); // ✅ 20
}

console.log(a); // ❌ Error: a is not defined
console.log(b); // ❌ Error: b is not defined

