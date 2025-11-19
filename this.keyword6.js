//Example Arrow Function

const user = {
  name: "Deepika",
  showName: () => {
    console.log(this.name); // 'this' does NOT refer to user
  }
};

user.showName(); 

//Example Normal Function
const user1 = {
  name: "Deepika",
  showName: function () {
    console.log(this.name); // 'this' refers to user object
  }
};

user1.showName(); // Output: Deepika

