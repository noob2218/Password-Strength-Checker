import string
Password = input("Enter Password: ")

uppercase = any([1 if c in string.ascii_uppercase else 0 for c in Password ])
lowercase = any([1 if c in string.ascii_lowercase else 0 for c in Password ])
specialchar = any([1 if c in string.punctuation else 0 for c in Password ])
digit = any([1 if c in string.digits else 0 for c in Password ])

conditions = [uppercase, lowercase, specialchar, digit]

length = len(Password)

score = 0

with open('common.txt', 'r') as f:
    common = f.read().splitlines()
if Password in common:
    print ("Password Exists")
    exit()

if length > 8:
    score += 1

if length > 12:
    score += 1
print(f"password length: {str(length)}, score: {str(score)}")


if sum(conditions) >= 1:
    score += 1
if sum(conditions) >= 2:
    score += 1
if sum(conditions) >= 3:
    score += 1
if sum(conditions) >= 4:
    score += 1


if score <= 1:
    print(f"Password is invalid, score is {str(score)}")
elif score <=3:
    print(f"Password is valid, but it is weak, score is {str(score)}")
elif score <=5:
    print(f"Password is valid, it is strong, score is {str(score)}")
elif score == 6 :
    print(f"Password is excellent and score is {str(score)}")





