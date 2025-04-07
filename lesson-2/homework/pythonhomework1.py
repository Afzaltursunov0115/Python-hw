
#   Number data type questions
# PROBLEM-1
float_num = float(input())
rounded_num=round(float_number, 2)
print(rounded)

# PROBLEM-2
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
third_num = int(input("Enter the third number: "))
print(max(first_num, second_num, third_num))
print(min(first_num, second_num, third_num))

# PROBLEM-3
km = 45
m = km*1000
cm = km*100000
print(m)
print(cm)

# PROBLEM-4
a = int(input())
b = int(input())
integer_part = int(a/b)
reminder = a/b-integer_part
print("Integer part:",integer_part)
print("Reminder:",reminder)


# PROBLEM-5
celcius = 20
fahrenheit = celcius*(9/5)+32
print(fahrenheit)

# PROBLEM-6
number = int(input())
last_digit = abs(number)%10
print(last_digit)

# PROBLEM-7
num1 = int(input("Enter the number: "))
if num1%2 == 0:
    print(f"{num1} is even")
else:
    print(f"{num1} is odd")

#    String data type questions
# PROBLEM-1
name = input("Enter your name: ")
year_of_birth = int(input("Enter your year of birth: "))
age = 2025-year_of_birth
print(f"Your age is {age}")

# PROBLEM-2

# PROBLEM-3
user_input = input("Enter a string: ")
print(f"The length of the string is: {len(user_input)}")
print(f"In uppercase letters: {user_input.upper()}")
print(f"In lowercase letters: {user_input.lower()}")

# PROBLEM-4
s = input("Enter a string: ")

if s == s[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# PROBLEM-5
st = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
for char in st:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")

# PROBLEM-6
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
if s2 in s1:
    print(f"'{s2}' is found in '{s1}'.")
else:
    print(f"'{s2}' is not found in '{s1}'.")

# PROBLEM-7
sentence = input("Enter a sentence: ")
replace_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")
new_sentence = sentence.replace(replace_word, new_word)
print(f"Updated sentence: {new_sentence}")

# PROBLEM-8
str = input("Enter a string: ")
if len(str) > 0:
    print(f"First character: {str[0]}")
    print(f"Last character: {str[-1]}")
else:
    print("The string is empty.")

# PROBLEM-9
st1 = input("Enter a string: ")
print(f"Reversed string: {st1[::-1]}")

# PROBLEM-10
sentence1 = input("Enter a sentence: ")
words = sentence1.split()
print(f"The number of words is: {len(words)}")

# PROBLEM-11
st2 = input("Enter a string: ")
if any(char2.isdigit() for char2 in st2):
    print("The string contains digits.")
else:
    print("The string does not contain digits.") 

# PROBLEM-12
words1 = input("Enter words separated by space: ").split()
separator = input("Enter a separator: ")
result = separator.join(words1)
print(f"Joined string: {result}")

# PROBLEM-13
st3 = input("Enter a string: ")
no_spaces = st3.replace(" ", "")
print(f"String without spaces: {no_spaces}")

# PROBLEM-14
st4 = input("Enter the first string: ")
st5 = input("Enter the second string: ")
if st4 == st5:
    print("The strings are equal.")
else:
    print("The strings are not equal.")


# PROBLEM-15
sentence4 = input("Enter a sentence: ")
acronym = "".join(word4[0].upper() for word4 in sentence4.split())
print(f"Acronym: {acronym}")

# PROBLEM-16
st5 = input("Enter a string: ")
char_to_remove = input("Enter the character to remove: ")
new_string = st5.replace(char_to_remove, "")
print(f"String without '{char_to_remove}': {new_string}")

# PROBLEM-17
st6 = input("Enter a string: ")
vowels6 = "aeiouAEIOU"
new_string6 = "".join("*" if char in vowels6 else char for char in st6)
print(f"String with vowels replaced: {new_string6}")

# PROBLEM-18
st7 = input("Enter a string: ")
start_word = input("Enter the start word: ")
end_word = input("Enter the end word: ")
if st7.startswith(start_word) and st7.endswith(end_word):
    print("The string starts with the first word and ends with the second word.")
else:
    print("The string doesn't match the start and end criteria.")


     # Boolean data type questions
# PROBLEM-1
username1 = input("Enter your username: ")
password1 = input("Enter your password: ")
if username1 and password1:
    print("Username and password are valid.")
else:
    print("Username or password cannot be empty.")

# PROBLEM-2
numb1 = float(input("Enter the first number: "))
numb2 = float(input("Enter the second number: "))
if numb1 == numb2:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

# PROBLEM-3
numb3 = float(input("Enter a number: "))
if numb3 > 0 and numb3 % 2 == 0:
    print("The number is positive and even.")
else:
    print("The number is not positive and even.")

# PROBLEM-4
numb4 = float(input("Enter the first number: "))
numb5 = float(input("Enter the second number: "))
numb6 = float(input("Enter the third number: "))
if numb4 != numb5 and numb4 != numb6 and numb5 != numb6:
    print("All three numbers are different.")
else:
    print("The numbers are not all different.")

# PROBLEM-5

strings1 = input("Enter the first string: ")
strings2 = input("Enter the second string: ")
if len(strings1) == len(strings2):
    print("The strings have the same length.")
else:
    print("The strings do not have the same length.")

# PROBLEM-6
numberx = int(input("Enter a number: "))
if numberx % 3 == 0 and numberx % 5 == 0:
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is not divisible by both 3 and 5.")
    
# PROBLEM-7
num01 = float(input("Enter the first number: "))
num02 = float(input("Enter the second number: "))
if num01 + num02 > 50.8:
    print("The sum of the numbers is greater than 50.8.")
else:
    print("The sum of the numbers is not greater than 50.8.")

# PROBLEM-8
num03 = float(input("Enter a number: "))
if 10 <= num03 <= 20:
    print("The number is between 10 and 20.")
else:
    print("The number is not between 10 and 20.")
