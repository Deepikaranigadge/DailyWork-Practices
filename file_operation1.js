// file system module ---> Write a file

const fs=require('fs');

let write_file = (file, contentToWrite)=>{
    fs.writeFile(file, contentToWrite, (err)=> {
        if(err){
            console.error("Error writing to file:",err);
            return;
        }
        console.log("Content successfully written to file");       
    });
}

let file_name2 = "file_operation1two.txt"
let some_content = "\n\nGood day!!"
write_file(file_name2, some_content)