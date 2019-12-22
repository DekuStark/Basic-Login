#--------------------
#BASIC USER LOGIN APP
#--------------------

#Process:
# Provide 2 user options: login and create user
# LOGIN: verify password matches username(case sensative)
# if login is successful, allow access to main home page of website
# if login is NOT successful, deny access

# create new account, append user and password to text file
# add second password input to verify password match
# if passwords matches, create account
# if they DO NOT, deny creation

# areas of improvement: add while loops, refine code, add security features, accessibility.

def main():
    userChoice = menuSelect()
    users, passwords = loadList()
    if userChoice == '1':
        loginUser(users,passwords)
    if userChoice == '2':
        createNewUser(users)
    input('Have a great day!\n')

def menuSelect():
    print('-----------------------')
    print('Welcome to your Website')
    print('-----------------------\n')
    print('1. Login')
    print('2. Create New Account')
    selection = input('Please enter your choice (1, 2, or leave blank to quit): ')
    print()
    if selection != '':
        if selection == '1' or selection == '2':
            return selection
        else:
            print('Please enter valid choice.\n')

def loadList():
    usernames = []
    passwords = []
    try:
        usersFile = open('users.txt', 'r')
    except IOError:
        print('Unable to open users.txt file')
    for line in usersFile:
        userInfo = line.split(',')
        usernames.append(userInfo[0])
        passwords.append(userInfo[1].rstrip())
    usersFile.close()
    return usernames, passwords

def loginUser(userList,passwdList):
    username = input('Username(Case sensitive): ' + '\n')
    password = input('Password: ' + '\n')
    if username in userList:
        findUser = userList.index(username)
        findPwd = passwdList[findUser]
        if password == findPwd:
            print('Login Successful!' + '\n')
        else:
            print('Login failed! - Password does not match our system.')
    else:
        print('Username not found.' + '\n')

def createNewUser(currentUserList):
    print('A username and password can be any length and will be case sensitive.\n')
    newUser = input('Create a username: ')
    if newUser not in currentUserList:
        newPwd = input('Create a new password: ')
        retypePwd = input('Re-type password: ')
        if newPwd == retypePwd:
            usersFiles = open('users.txt', 'a')
            usersFiles.write(newUser + ',' + newPwd + '\n')
            usersFiles.close()
            print('You have successfully created a new account! Login now to enjoy!')
        else:
            print('Passwords do not match.')
    else:
        print('Username already in use.')

main()