import random

database_user = {
    'Seyi':'passwordSeyi',
    'Mike':'passwordMike',
    'Love':'passwordLove'
}


def __init__():

    print("Welcome, what would you like to do?")
    print("1. Login")
    print("2. Register")

    select_option = int(input("Select an option \n"))
    if(select_option == 1):
        isLoginSuccessful = False

        while isLoginSuccessful == False:
            isLoginSuccessful = login()

    

        bankOperations()

    elif(select_option == 2):
            register()

 
           
    else:
        print('Login failed, username or password incorrect')


  


def login():
    #login function
    print('*********login***********')
    name = input("What is your name? \n")
    password = input("Your password? \n")
    if(name in database_user and password == database_user[name]):
        print('Welcome %s' % name)

  
        from datetime import date
        today = date.today()
        currentDate = today.strftime('%d:%m:%Y')
        print('Date - ', currentDate)
        import time
        t = time.localtime()
        currentTime = time.strftime('%H:%M:%S', t)
        print('Time - ', currentTime)

        bankOperations()



        
    else:
        print("Password or Username Incorrect. Please try again")

        login()
        



def register():
    print('Register')
    email = input('what is your email address? \n')
    first_name = input('what is your first name? \n')
    last_name = input('what is your last name? \n')
    password = input('create a password \n')


    accountNumber = generateAccountNumber()

    database_user[accountNumber] = [first_name, last_name, email, password]

    print('your account has been created')
    print('== ============ =======')
    print('your account number is: %d' % accountNumber)
    print('Make sure you keep it safe')
    print('== ============ =======')
    


    login()


def bankOperations():

        print('These are the available option:')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')
        print('4. Logout')

        selectedOption = int(input('please select an option: \n'))

        accountBalance = 50000
       
        

        if(selectedOption == 1):
            print('How much would you like to withdraw?')

            amountWithdraw = int(input('please enter amountWithdraw: \n'))

            currentBalance = (accountBalance - amountWithdraw)

            
            print('Withdraw succesful!!!')
            print('Your new balance is %s' % currentBalance)
            print('Take your cash')
            print('would you like to carry out more transactions? \n')

            more_trasxn = int(input('Do you want to carry out more transactions?: 1 (yes) 2 (no) \n'))
            if(more_trasxn == 1):
                bankOperations()
            elif(more_trasxn == 2):
                exit()

            
            
        elif(selectedOption == 2):
             print('How much would you like to deposit?')

             amountDeposit = int(input('please enter amountDeposit: \n'))

             currentBalance = (accountBalance + amountDeposit)
             

             print('Deposit succesful.Your new balance is %s' % currentBalance)
             print('would you like to carry out more transactions? \n')

             more_trasxn = int(input('Do you want to carry out more transactions?: 1 (yes) 2 (no) \n'))
             if(more_trasxn == 1):
                 bankOperations()
             elif(more_trasxn == 2):
                 exit()




        elif(selectedOption == 3):
             print('What issue would you like to report?')

             print('Select from the options below:')
             print('1. Failed Withdrawal')
             print('2. Card Issues')
             print('3. General complaints')

             selectedOption = int(input('please select an option: \n'))

             
             if(selectedOption == 1):
              print('Thank you for contacting us, your complaint would be resolved shortly')
              more_trasxn = int(input('Do you want to carry out more transactions?: 1 (yes) 2 (no) \n'))
              if(more_trasxn == 1):
                 bankOperations()
              elif(more_trasxn == 2):
                  exit()



        elif(selectedOption == 4):
             login()

 
        else:
            print('Invalid Option, please try again')


def generateAccountNumber():
    return random.randrange(1111111111,9999999999)
    



__init__()

            
            
  
