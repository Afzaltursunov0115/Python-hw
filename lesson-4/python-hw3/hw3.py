# Questions
# 2)continue: skips the current iteration and moves to the next one.
#   break: exits the loop completely.
# 3)for loop: used when the number of iterations is known (e.g., iterating over a list or range).
#   while loop: used when the condition is based on logic rather than a set number of repetitions.
# 4)for i in range(3):
#   for j in range(2):
#       print(f"i={i}, j={j}")


# Homeworks
import random

# PROBLEM-1
list1 = [1, 1, 2]
list2 = [2, 3, 4]
result = []

for i in list1:
    if i not in list2:
        result.append(i)

for i in list2:
    if i not in list1:
        result.append(i)

print(result)

# PROBLEM-2
n = 5
for i in range(1, n):
    print(i * i)

# PROBLEM-3
txt = "abcabcdabcdeabcdefabcdefg"
result = ""
count = 0

for i in range(len(txt)):
    result += txt[i]
    count += 1
    if count == 3 and i != len(txt) - 1 and txt[i] not in 'aeiou':
        result += "_"
        count = 0

print(result)

# PROBLEM-4
while True:
    number = random.randint(1, 100)
    attempts = 0

    while attempts < 10:
        guess = int(input("Guess the number (1-100): "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("You guessed it right!")
            break
        attempts += 1

    if attempts == 10:
        print("You lost. Want to play again?")
        again = input("Type 'yes' to play again: ")
        if again.lower() not in ['y', 'yes', 'ok']:
            break
    else:
        break

# PROBLEM-5
password = input("Enter password: ")

if len(password) < 8:
    print("Password is too short.")
elif not any(char.isupper() for char in password):
    print("Password must contain an uppercase letter.")
else:
    print("Password is strong.")

# PROBLEM-6
for num in range(2, 101):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

# PROBLEM-7
player_score = 0
computer_score = 0
choices = ['rock', 'paper', 'scissors']

while player_score < 5 and computer_score < 5:
    player = input("Enter rock, paper, or scissors: ").lower()
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a draw!")
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print(f"Score: You {player_score} - {computer_score} Computer")

if player_score == 5:
    print("You win the match!")
else:
    print("Computer wins the match!")
