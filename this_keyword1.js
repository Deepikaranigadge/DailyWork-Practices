//this inside an object method

const user = {
  name: "Deepika",
  role: "Developer",
  getDetails() {
    return `${this.name} is a ${this.role}`;
  }
};

console.log(user.getDetails());