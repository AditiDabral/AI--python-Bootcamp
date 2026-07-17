# count words and lines in a file 
def count_words(file_name):
     try:
         with open(file_name,"r") as file:
             lines = file.readlines()
             line_count= len(lines)
             word_count = sum(len(line.split()) for line in lines)
             
             print(f"Numbers of lines :{line_count}")
             print(f"Numbers of words: {word_count}")
     except FileNotFoundError:
         print(f"file {file_name} not found")
        
count_words("week 1/Myfile.txt")
             
             