//this with .call()

function greet(city, country) {
  console.log(`Hello ${this.name} from ${city}, ${country}`);
}

const user = { name: "Deepika" };

greet.call(user, "Delhi", "India");

//this with .apply()

function greet(city, country) {
  console.log(`Hello ${this.name} from ${city}, ${country}`);
}

const user1 = { name: "Deepika" };

greet.apply(user1, ["Mumbai", "India"]);

//this with .bind()

function greet() {
  console.log(`Hello ${this.name}`);
}

const user2 = { name: "Deepika" };

const newFunc = greet.bind(user2);
newFunc();  // calling manually

