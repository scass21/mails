import random
import re


def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[2] + '.' + i[1][1:letter] + '@company.io' in emails:
            letter += 1
        emails.append(i[2] + '.' + i[1][1:letter] + '@company.io')
    for i in range(len(emails)):
        list_of_names[i][0] = emails[i]
    return list_of_names


def password_generator(length):
    if length < 12:
        return print('Error')
    password = [random.choice('1234567890'), random.choice('abcdefghijklmnopqrstuvwxyz'),
                random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), random.choice('!@#$%^&*()-+')]
    while len(password) < length:
        password.append(random.choice('1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-+'))
    random.shuffle(password)
    pwd = ''.join(password)
    return pwd

#############################


file = open('task_file.txt')
s = file.readlines()
file.close()
for i in range(len(s)):
    s[i] = s[i].split(', ')
error_strings = []
list_of_names = []
check_name = r'^[A-Z][a-z]+'
check_tel = r'\d{7}'
check_city = r'^[A-Z][a-zA-Z.]+[\n]'
for i in range(len(s)):
    if re.fullmatch(check_name, s[i][1]) and re.fullmatch(check_name, s[i][2]) \
            and re.fullmatch(check_tel, s[i][3]) and re.fullmatch(check_city, s[i][4]):
        list_of_names.append(s[i])
    else:
        error_strings.append(s[i])
f = open('error_str.txt', 'w')
for element in error_strings:
    f.write(", ".join((str(i) for i in element)))
f.close()

new_list = email_gen(list_of_names)
for i in range(len(new_list)):
    new_list[i].insert(1, password_generator(12))
new_file = open('task_file.txt', 'w')
new_file.write('EMAIL, PASSWORD, NAME, LAST_NAME, TEL, CITY\n')
for element in new_list:
    new_file.write(", ".join((str(i) for i in element)))
new_file.close()

