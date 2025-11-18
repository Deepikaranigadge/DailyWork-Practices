function BankAccount(balance) {
  this.balance = balance;
}

BankAccount.prototype.deposit = function (amount) {
  this.balance += amount;
  return this.balance;
};

const acc1 = new BankAccount(1000);
const acc2 = new BankAccount(500);

console.log(acc1.deposit(200)); // 1200
console.log(acc2.deposit(300)); // 800
