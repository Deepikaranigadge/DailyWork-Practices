//Using async/await with try...catch(Error Handling)

async function fetchData(){
    try{
        let promise = new Promise((_, reject)=> {
            setTimeout(()=> reject("Error fetching data"), 2000);
        });
        let result = await promise;
        console.log(result);
    }
    catch(error){
        console.log("Caught Error: ",error);
    }
}
fetchData();
