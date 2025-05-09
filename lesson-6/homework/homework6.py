# PROBLEM-1
def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper

@check
def div(a, b):
    return a / b

# PROBLEM-2
def add_employee():
    with open("employees.txt", "a") as f:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        f.write(f"{emp_id}, {name}, {position}, {salary}\n")
        print("Record added.\n")

def view_all():
    try:
        with open("employees.txt", "r") as f:
            print("\nAll Employees:")
            print(f.read())
    except FileNotFoundError:
        print("No records found.\n")

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False
    with open("employees.txt", "r") as f:
        for line in f:
            if line.startswith(emp_id + ","):
                print("Record found:", line.strip())
                found = True
                break
    if not found:
        print("Employee not found.\n")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    updated = False
    lines = []
    with open("employees.txt", "r") as f:
        lines = f.readlines()
    with open("employees.txt", "w") as f:
        for line in lines:
            if line.startswith(emp_id + ","):
                name = input("Enter new name: ")
                position = input("Enter new position: ")
                salary = input("Enter new salary: ")
                f.write(f"{emp_id}, {name}, {position}, {salary}\n")
                updated = True
            else:
                f.write(line)
    if updated:
        print("Employee updated.\n")
    else:
        print("Employee not found.\n")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    deleted = False
    lines = []
    with open("employees.txt", "r") as f:
        lines = f.readlines()
    with open("employees.txt", "w") as f:
        for line in lines:
            if not line.startswith(emp_id + ","):
                f.write(line)
            else:
                deleted = True
    if deleted:
        print("Employee deleted.\n")
    else:
        print("Employee not found.\n")

while True:
    print("1. Add new employee record")
    print("2. View all employee records")
    print("3. Search for an employee by ID")
    print("4. Update an employee")
    print("5. Delete an employee")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_all()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        update_employee()
    elif choice == "5":
        delete_employee()
    elif choice == "6":
        break
    else:
        print("Invalid choice.\n")

# PROBLEM-3
import os
import string
from collections import Counter

# Create sample.txt if not exists
if not os.path.exists("sample.txt"):
    print("sample.txt not found. Please type a paragraph:")
    with open("sample.txt", "w") as f:
        f.write(input("Enter text: "))

# Read content
with open("sample.txt", "r") as f:
    text = f.read()

# Clean and process
text = text.lower()
for p in string.punctuation:
    text = text.replace(p, "")
words = text.split()

# Count words
word_counts = Counter(words)
total_words = len(words)
most_common = word_counts.most_common(5)

# Print result
print(f"\nTotal words: {total_words}")
print("Top 5 most common words:")
for word, count in most_common:
    print(f"{word} - {count} times")

# Save to report
with open("word_count_report.txt", "w") as f:
    f.write("Word Count Report\n")
    f.write(f"Total Words: {total_words}\n")
    f.write("Top 5 Words:\n")
    for word, count in most_common:
        f.write(f"{word} - {count}\n")
