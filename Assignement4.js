//Async with Multiple await Statements

async function processData(){
    console.log("Fetching user...");
    await new Promise((res)=> setTimeout(res, 1000));

    console.log("Fetching orders...");
    await new Promise((res)=> setTimeout(res, 1000));

    console.log("Fetching payment...");
    await new Promise((res)=> setTimeout(res, 1000));

    console.log("All data featched");
}
processData();