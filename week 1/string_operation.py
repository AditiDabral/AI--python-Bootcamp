def reversed(text):
    return text[::-1]

def countvowels(text):
    vowels="aeiou"
    count =0
    for char in text :
        if char in vowels:
            count+=1
    return count 

def palindrome(text):
     # Clean the string: convert to lowercase and remove spaces
    cleaned_text = "".join(text.lower().split())
    
    # Check if the cleaned text matches its reversed version
    return cleaned_text == cleaned_text[::-1]