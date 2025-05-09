# PROBLEM-1
def convert_cel_to_far(c):
    return round(c * 9 / 5 + 32, 2)

def convert_far_to_cel(f):
    return round((f - 32) * 5 / 9, 2)

f = float(input("Enter a temperature in degrees F: "))
c_result = convert_far_to_cel(f)
print(f"{f} degrees F = {c_result} degrees C")

c = float(input("\nEnter a temperature in degrees C: "))
f_result = convert_cel_to_far(c)
print(f"{c} degrees C = {f_result} degrees F")

# PROBLEM-2
def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount = amount * (1 + rate)
        print(f"year {year}: ${amount:.2f}")

amount = float(input("Enter initial amount: "))
rate = float(input("Enter annual rate (e.g. 0.05 for 5%): "))
years = int(input("Enter number of years: "))

invest(amount, rate, years)

# PROBLEM-3
n = int(input("Enter a positive integer: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(f"{i} is a factor of {n}")

# PROBLEM-4
universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(unis):
    students = []
    tuition = []
    for uni in unis:
        students.append(uni[1])
        tuition.append(uni[2])
    return students, tuition

def mean(lst):
    return sum(lst) / len(lst)

def median(lst):
    sorted_list = sorted(lst)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:
        return sorted_list[mid]

students, tuition = enrollment_stats(universities)

print("*" * 30)
print(f"Total students: {sum(students):,}")
print(f"Total tuition: $ {sum(tuition):,}\n")

print(f"Student mean: {mean(students):,.2f}")
print(f"Student median: {int(median(students))}\n")

print(f"Tuition mean: $ {mean(tuition):,.2f}")
print(f"Tuition median: $ {int(median(tuition))}")
print("*" * 30)
        
# PROBLEM-5
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
num = int(input("Enter a number to check if it's prime: "))
if is_prime(num):
    print("It is a prime number.")
else:
    print("It is not a prime number.")
