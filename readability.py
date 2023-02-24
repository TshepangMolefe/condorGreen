#Implement a program that computes the approximate grade level needed to comprehend some text, per the below.

from cs50 import get_string       # since string is not native to python


#while True:
text = get_string("text: ")       #// prompt user for text input
     #if len(text) > 0:            # calculate the length of the string in the text
       # break

letters = 0
words = 1                             # to account for the last word in the text that does not have a space after that
sentences = 0

for i in text:                 # loop through text, counting number of characters in the text
    if i in [".", "!", "?"]:    #// count the number of sentences that are there in the text
        sentences += 1
    elif  i.isspace():           #// count the number of words that are there in the text "returns True if all the characters in a string are whitespaces, otherwise False.""
        words += 1
    elif  i.isalpha():           #// count the number of letters that are there in the text function returns True if all characters in the string are alphabets (can be both lowercase and uppercase)
        letters += 1

#print(f"letters: {letters}")       # printing output number of words, letters and sentences
#print(f"Sentences: {sentences}")
#print(f"words: {words}")

L = letters /  words * 100          # where L is the average number of letters per 100 words in the text.
S = sentences / words * 100         # S is the average number of sentences per 100 words in the text. in python division sign give us float output

                                   #The round() function returns a floating point number that is a rounded version of the specified number,
                                   #with the specified number of decimals. the function will return the nearest integer

index = round(0.0588 * L - 0.296 * S - 15.8)     #coleman-liau index formular  # Now it’s time to put all pieces together!
if index < 1:
    print("Before Grade 1")                       #returns a floating point number that is a rounded version of the specified number, with the specified number of decimals
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")

    # this formatted string does: it looks for {} & inters variables inside values of variables inside them.
    #print("Grade index")




















