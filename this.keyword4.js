//this in arrow functions

const user = {
  name: "Deepika",
  showName() {
    setTimeout(() => {
      console.log(this.name);
    }, 1000);
  }
};

user.showName();  

