import re
import string

blacklist = ['123456','12345','123456789','password','iloveyou','princess','1234567','rockyou','12345678','abc123', \
              '1234','12345678', 'qwerty','111111','000000','password1','Password','secret','121212',\
              '000000','7777777','Password1']


def get_password_strength(password): #checks the strength
    p = password
    count = 0
    if p in blacklist or len(p) == 1:
        count = 1
    if len(re.findall('\d', p)) > 0:
        count += 1
    if len(re.findall('[A-Z]', p)) > 0:
        count += 1
    if len(re.findall('[a-z]', p)) > 0:
        count += 1
    if len(re.findall('[^a-zA-Z0-9]', p)) > 0:
        count += 1
    if len(p) > 3:
        count += 1
    if len(p) > 5:
        count += 1
    if len(p) > 7:
        count += 1
    if len(p) > 9:
        count += 1
    if len(p) > 11:
        count += 1
    if len(p) > 13:
        count += 1
    return count


def main():
    password = input("Enter your password:\n")
    if len(password)>0 and len(re.findall('\s',password)) == 0: #checks if password consist only of printable symbols
        print('Your score:', get_password_strength(password))
    else:
        print('Password length must be > 0 and it should consists only of printable symbols')


if __name__ == '__main__':
        main()
