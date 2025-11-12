// Append a file system

const fs=require('fs');

let append_file = (file, contentToAppend)=>{
    fs.appendFile(file, contentToAppend, (err)=> {
        if(err){
            console.error("Error appending to file:",err);
            return;
        }
        console.log("Content successfully appended to file");       
    });
}

let file_name2 = "file.operation1two.txt"
let some_content = "\n\nGreate day!!"
append_file(file_name2, some_content)