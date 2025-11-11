// file system module ---> Read a file

const fs=require('fs');

let read_file = (file)=>{
    fs.readFile(file, 'utf8', (err, data)=> {
        if(err){
            console.error("Error reading file:",err);
            return;
        }
        console.log("file content:");
        console.log(data);
    });
}

let file_name1 = "file_operationone.txt"
read_file(file_name1)