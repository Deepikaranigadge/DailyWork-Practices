//Using await inside an async function

async function getMessage(){
    let promise = new Promise((resolve)=> {
        setTimeout(()=>resolve("Data received"), 2000);
    });
    let result = await promise;
    console.log(result);
}
getMessage();