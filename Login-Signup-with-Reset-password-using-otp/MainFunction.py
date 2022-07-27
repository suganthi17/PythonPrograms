while 1:    
    mode = input("""
    Press 1 for Signup
    Press 2 for Login
    Press 0 to Exit
    : """)
    if mode == '1':
        print('Signup -', signUp())
    
    elif mode == '2':
        print('Login -', login())
    #     logIn()
    
    elif mode == '0':
        print('Thank you.\nExiting...')
        break

    else:
        print("Invalid input...")
