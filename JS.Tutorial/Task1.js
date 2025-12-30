let marks = 45

switch (true) {
  case (marks >= 80 && marks <= 100):
    console.log("Distinction");
    break;

  case (marks >= 60 && marks <= 79):
    console.log("First Class");
    break;

  case (marks >= 50 && marks <= 59):
    console.log("Second Class");
    break;

  case (marks >= 35 && marks <= 49):
    console.log("Pass");
    break;

  case (marks >= 0 && marks < 35):
    console.log("Fail");
    break;

  default:
    console.log("Invalid Marks");
}
