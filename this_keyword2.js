//this inside a constructor function / class

class Product {
  constructor(name, price) {
    this.name = name;
    this.price = price;
  }

  getInfo() {
    return `${this.name} costs ₹${this.price}`;
  }
}

const laptop = new Product("Dell Laptop", 55000);

console.log(laptop.getInfo());