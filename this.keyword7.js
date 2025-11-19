//Arrow function inside normal function

function Person(name) {
  this.name = name;

  setTimeout(function () {
    console.log("Normal:", this.name);
  }, 500);

  setTimeout(() => {
    console.log("Arrow:", this.name);
  }, 500);
}

new Person("Deepika");
