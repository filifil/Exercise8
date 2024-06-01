# EXERCISE 1.1
def get_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
#example1.1
numbers=[12,34,45,67,89]
result=get_sum(numbers)
print(result)


# Exercise 1.2
def remove_duplicates(numbers):
    return list(set(numbers))

# Exercise 1.3
numbers = [1, 2, 3, 4, 4, 3, 2, 1]
print(get_sum(remove_duplicates(numbers)))

# Exercise 2
def create_list(start, end):
    return list(range(start, end+1))

# Exercise 3.1
def get_alphabet_number(letter):
    return ord(letter) - 96

# Exercise 3.2
def is_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return set(sentence.lower()) >= alphabet

# Exercise 4
def check_vowel_consonant(letter):
    vowels = 'aeiou'
    if letter.lower() in vowels:
        return 'vowel'
    else:
        return 'consonant'

user_input = input("Enter a string: ")
vowels = 0
consonants = 0
for letter in user_input:
    if letter.isalpha():
        if check_vowel_consonant(letter) == 'vowel':
            vowels += 1
        else:
            consonants += 1
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)

# Exercise 5
def is_armstrong(num):
    num_str = str(num)
    power = len(num_str)
    armstrong = sum(int(digit)**power for digit in num_str)
    return armstrong == num

user_num = int(input("Enter a number: "))
for i in range(user_num + 1):
    if len(str(i)) > 2 and is_armstrong(i):
        print(i)



