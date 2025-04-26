import string
import random
# letters = string.ascii_lowercase
# random_letter = random.choice(letters)
# # print(random_letter)            this was just my first attempt at trying to get the code to print a letter in general
# letter_amount = 0 
# for eachLetter in letters:        then i was trying to make a for loop that would go through the 26 letters of the english alphabet. then I realized ascii doesn't stand for American Standard something something language something
    #                               regardless, it would have been silly
#     letter_amount = + 1           my idea was to put a similar code to what we used for the midterm, where we had a repetition for draw this while this but I could not 
#                                       figure out how to get the code to add the letters to a Something

# print(letter_amount)

random_string = '' #                this where it got strange to me. I would have never thought about having to add a blank space before
#                                   I am still curious, I thought that the order in which inputs were given to a code really mattered, so why does this one have to start as en empty string? I would think that that woud add a space to the product when you run the program but alas
letter_amount = 0

while letter_amount < 12:
    random_string += random.choice(string.ascii_lowercase)
    letter_amount += 1

print(random_string)