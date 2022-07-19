import json

log_or_reg = input('Login or registration? ')

login = input('Login: ')
password = input('Password: ')
data = {'log': login, 'passwd': password}

if log_or_reg == 'login':
    def login_function(login, password):
        with open('reg.json', 'r') as f:
            data = json.load(f)
        if data[login] == password:
            print('Successful login')
        else:
            print('Wrong login or password')
            q1 = input('Try again? ')
            if q1 == 'yes':
                login = input('Login: ')
                password = input('Password: ')
                login_function(login, password)

    login_function(login, password)

else:
    def registration(login, password):
        with open('reg.json', 'r') as f:
            data = json.load(f)
        if login not in data.keys():
            data[login] = password
            with open('reg.json', 'w') as f:
                return json.dump(data, f)
        else:
            print('This login already exists')
            q2 = input('Try again? ')
            if q2 == 'yes':
                login = input('Login: ')
                password = input('Password: ')
                registration(login, password)

    registration(login, password)