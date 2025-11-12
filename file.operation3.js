// delete a file system

const fs=require('fs');

let delete_file = (file)=>{
    fs.unlink(file, (err)=> {
        if(err){
            console.error("Error deleting to file:",err);
            return;
        }
        console.log("File deleted successfully");       
    });
}

let file_name2 = "file.operation3two.txt"
let some_content = "\n\nGreate day!!"
delete_file(file_name2)