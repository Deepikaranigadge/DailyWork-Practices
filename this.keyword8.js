//this in ES6 Class

class User {
  constructor(name) {
    this.name = name;
  }
  show() {
    console.log(this.name);
  }
}

const u = new User("Deepika");
u.show(); // Deepika
