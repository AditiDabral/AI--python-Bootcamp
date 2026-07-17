# opening a file : by default a file is open in read only mode 
# r = read mode , w = write mode  (overwrite the file if already exit ) , a = append (adds data at the end of file ) , r+ = read and write 

# reading file : .read()= read whole file , readline = read specfice line or one line [ it walys use with loop for reading lines oneat  time  ] , readlines = give a list of content of each line 

with open("sample.txt","r") as file :  # with statement : it ensure that what u have opened the file are properly closed after the operation 
    
    content = file.read()
    print(content)
    
    
# writing a file : write(),writelines()

with open("sample.txt","w") as file :
    file.write["hello world !"]
    file.writelines(["Alice","Bob","Priya"])
    
# file is automatically closed : advantages 1) simplifes code 2) reduces the risk of file corruption 

###### Exception handling :prevents the program from crashing due to file related errors (eg: file not found , file corrupt)

## try except block 

try :
    with open("sample2.txt","r") as file2:
        content = file.read()
except:
    print("File Not Found")
    
# common file handling exception : FileNotFoundError , Permission Error , IOError : input output error
        