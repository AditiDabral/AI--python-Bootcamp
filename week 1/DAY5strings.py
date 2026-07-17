#CONCATENATION
first_name = "Priya"
Last_name = "Jha"
full_name = first_name +" "+Last_name
print(full_name)

# slicing 
print(full_name[-5:])

#formating
name = "Jira"
age = 14
print(f"my name is {name} and my age is {age}")

#split() : into a list 
sentence = "python is fun"
words = sentence.split()
print(words)

#join() : join elements of list into a single string 
new_sentence = "|".join(words)
print(new_sentence)

#replace()
text = "I love Python"
updated_text = text.replace("Python", "Java")
print(updated_text)

#strip : default it will remove alll spaces 
messy = "     HI how are you   "
cleaned_text = messy.strip()
print(cleaned_text)

##################### REgular expression for pattern making : it will search the pattern , and u can also do some changes by using re module

import re
random_text = " Contact me at 232-324-654 "
digits = re.findall(r"\d+",random_text)
print(digits)

update_random = re.sub(r"\d","X",random_text)  # substituting 
print(update_random)
print(re.search(r"X",update_random))


#cleaning a text 

def clean_text(text):
    # remove punctuation
    text = re.sub(r"[^\w\s]","",text)
    
    #remove exta spaces 
    text = " ".join(text.split())
    
    # convert to lowercase
    return text.lower()

input_text = input("Enter your text")
print(clean_text(input_text    ))
    
 
